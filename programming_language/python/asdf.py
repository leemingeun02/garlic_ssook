import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import json
import re
import mysql.connector
import time

# 데이터베이스 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'kimtrack@',
    'database': 'web_crawler'
}

def fetch_and_store_data(url):
    # Selenium 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_service = Service(ChromeDriverManager().install())

    # 웹 드라이버 시작
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(url)

    def get_text(by, selector, default=None):
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, selector)))
            return element.text.strip() if element.text.strip() else default
        except:
            return default

    def get_attribute(by, selector, attribute, default=None):
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, selector)))
            return element.get_attribute(attribute).strip() if element.get_attribute(attribute).strip() else default
        except:
            return default

    def parse_post_time(post_time_str):
        now = datetime.now()
        if not post_time_str:
            return None
        if '분전' in post_time_str:
            minutes = int(re.search(r'\d+', post_time_str).group())
            return now - timedelta(minutes=minutes)
        elif '시간전' in post_time_str:
            hours = int(re.search(r'\d+', post_time_str).group())
            return now - timedelta(hours=hours)
        elif '일전' in post_time_str:
            days = int(re.search(r'\d+', post_time_str).group())
            return now - timedelta(days=days)
        else:
            return now

    def extract_counts(post_time_full):
        if not post_time_full:
            return None, None, None
        views, chats, favorites = None, None, None
        try:
            counts_text = post_time_full.split('·')[1:]
            for count in counts_text:
                if '조회' in count:
                    views = int(count.split('조회')[1].strip())
                elif '채팅' in count:
                    chats = int(count.split('채팅')[1].strip())
                elif '찜' in count:
                    favorites = int(count.split('찜')[1].strip())
        except:
            pass
        return views, chats, favorites

    def get_image_urls():
        image_urls = set()
        max_images = 10
        wait = WebDriverWait(driver, 5)
        while len(image_urls) < max_images:
            try:
                image_url = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.swiper-slide-active img'))).get_attribute('src')
                if image_url:
                    image_urls.add(image_url)
                
                if len(image_urls) < max_images:
                    next_button = wait.until(EC.element_to_be_clickable((By.ID, 'product-gallery-slider-next')))
                    driver.execute_script("arguments[0].click();", next_button)
            except:
                break
        return list(image_urls)

    try:
        title = get_text(By.CSS_SELECTOR, 'h1.text-lg.font-semibold, h1.md\\:text-2xl')
        price_text = get_text(By.CSS_SELECTOR, 'div.font-bold.md\\:text-\\[32px\\]')
        price = int(''.join(filter(str.isdigit, price_text))) if price_text else None

        post_time_full = get_text(By.CSS_SELECTOR, 'span.text-jnGray-500.leading-\\[15px\\]')
        post_time_str = post_time_full.split('·')[0].strip() if post_time_full else ''
        post_time = parse_post_time(post_time_str).strftime('%Y-%m-%d %H:%M:%S') if post_time_str else None

        views, chats, favorites = extract_counts(post_time_full)
        product_condition = get_text(By.CSS_SELECTOR, 'button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1')
        transaction_method = get_text(By.XPATH, '//span[text()="거래방식"]/following-sibling::button[@disabled]')
        shipping_included = get_text(By.XPATH, '//span[text()="배송비"]/following-sibling::button[@disabled]')
        safe_transaction = get_text(By.XPATH, '//span[text()="안전거래"]/following-sibling::button[@disabled]')
        product_info = get_text(By.CSS_SELECTOR, 'p.flex-1.py-5.text-base.font-normal.break-words.break-all.whitespace-pre-line.text-jnGray-900')
        seller_id = get_attribute(By.CSS_SELECTOR, 'a.flex.items-center.justify-between.w-full.pt-5.lg\\:pt-\\[28px\\].lg\\:pb-5', 'href')
        seller_nickname = get_text(By.CSS_SELECTOR, 'a.flex.items-center.justify-between.w-full.pt-5.lg\\:pt-\\[28px\\].lg\\:pb-5 p.text-\\[22px\\]')
        trust_score = get_text(By.CSS_SELECTOR, 'span.ml-1.text-lg.font-semibold')
        safe_transaction_count = get_text(By.XPATH, '//ul[@class="box-border flex text-center border border-gray-300 rounded items-center py-[18px] mt-5"]//li[span[text()="안전거래"]]/button[@disabled]')
        reviews_count = get_text(By.CSS_SELECTOR, 'button.block.text-sm.font-semibold.text-jnblack.mt-1.underline')
        loyal_customers_count = get_text(By.XPATH, '//span[text()="단골"]/following-sibling::button[@disabled]')

        image_urls = get_image_urls()

        def insert_data(data):
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            query = """
            INSERT INTO joongna (title, price, post_time, views, chats, favorites, product_condition, transaction_method,
                                shipping_included, safe_transaction, product_info, seller_id, seller_nickname, trust_score,
                                safe_transaction_count, reviews_count, loyal_customers_count, image_urls, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            image_urls_json = json.dumps(image_urls) if image_urls else None

            data_to_insert = (title, price, post_time, views, chats, favorites, product_condition, transaction_method,
                              shipping_included, safe_transaction, product_info, seller_id, seller_nickname, trust_score,
                              safe_transaction_count, reviews_count, loyal_customers_count, image_urls_json, url)

            cursor.execute(query, data_to_insert)
            connection.commit()
            cursor.close()
            connection.close()

        insert_data((title, price, post_time, views, chats, favorites, product_condition, transaction_method,
                     shipping_included, safe_transaction, product_info, seller_id, seller_nickname, trust_score,
                     safe_transaction_count, reviews_count, loyal_customers_count, image_urls, url))
    except Exception as e:
        print(f"Error processing URL {url}: {e}")
    
    driver.quit()

def main():
    base_url = 'https://web.joongna.com/product/'
    start_id = 178529052
    num_threads = 50
    thread_list = []

    while True:
        for i in range(num_threads):
            url = f"{base_url}{start_id + i}"
            thread = threading.Thread(target=fetch_and_store_data, args=(url,))
            thread_list.append(thread)
            thread.start()
            time.sleep(0.1)  # 잠시 대기하여 서버 부하를 줄입니다.

        for thread in thread_list:
            thread.join()

        start_id += num_threads
        thread_list.clear()

if __name__ == "__main__":
    main()