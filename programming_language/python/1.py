from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Selenium 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # GUI를 띄우지 않는 headless 모드
chrome_service = Service(ChromeDriverManager().install())

# 웹 드라이버 시작
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 크롤링할 URL
url = 'https://web.joongna.com/product/177842713'
driver.get(url)

# 페이지 로딩 대기
time.sleep(0.9)  # 필요에 따라 로딩 시간을 조절

# 요소 추출 함수
def get_text_or_default(by, selector, default=''):
    try:
        element = driver.find_element(by, selector)
        return element.text.strip()
    except:
        return default

def get_text_by_xpath_or_default(xpath, default=''):
    try:
        element = driver.find_element(By.XPATH, xpath)
        return element.text.strip()
    except:
        return default

# 제목 추출
title = get_text_or_default(By.CSS_SELECTOR, 'h1.text-lg.font-semibold, h1.md\\:text-2xl')

# 가격 추출
price = get_text_or_default(By.CSS_SELECTOR, 'div.font-bold.md\\:text-\\[32px\\]')

# 작성 시간 추출
post_time_full = get_text_or_default(By.CSS_SELECTOR, 'span.text-jnGray-500.leading-\\[15px\\]')
post_time = post_time_full.split('·')[0].strip() if post_time_full else ''

# 조회수, 채팅수, 찜수 추출
def extract_counts(post_time_full):
    views, chats, favorites = 0, 0, 0
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

views, chats, favorites = extract_counts(post_time_full)

# 제품 상태 추출
product_condition = get_text_or_default(By.CSS_SELECTOR, 'button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1')

# 거래 방식 추출
transaction_method = get_text_by_xpath_or_default('//span[text()="거래방식"]/following-sibling::button[@disabled]', '')

# 배송비 포함 여부 추출
shipping_included = get_text_by_xpath_or_default('//span[text()="배송비"]/following-sibling::button[@disabled]', '')

# 안전 거래 사용 여부 추출
safe_transaction = get_text_by_xpath_or_default('//span[text()="안전거래"]/following-sibling::button[@disabled]', '')

# 상품 정보 추출
product_info = get_text_or_default(By.CSS_SELECTOR, 'p.flex-1.py-5.text-base.font-normal.break-words.break-all.whitespace-pre-line.text-jnGray-900')

# 판매자 정보 추출 (ID, 닉네임)
seller_info = driver.find_element(By.CSS_SELECTOR, 'a.flex.items-center.justify-between.w-full.pt-5.lg\\:pt-\\[28px\\].lg\\:pb-5')
if seller_info:
    seller_id = seller_info.get_attribute('href')
    seller_nickname = seller_info.find_element(By.CSS_SELECTOR, 'p.text-\\[22px\\]').text.strip()
else:
    seller_id = ''
    seller_nickname = ''

# 신뢰지수 추출
trust_score = get_text_or_default(By.CSS_SELECTOR, 'span.ml-1.text-lg.font-semibold')

# 안전 거래 횟수 추출
safe_transaction_count = get_text_by_xpath_or_default('//ul[@class="box-border flex text-center border border-gray-300 rounded items-center py-[18px] mt-5"]//li[span[text()="안전거래"]]/button[@disabled]', '0')

# 거래 후기 수 추출
reviews_count = get_text_or_default(By.CSS_SELECTOR, 'button.block.text-sm.font-semibold.text-jnblack.mt-1.underline')

# 단골 수 추출
loyal_customers_count = get_text_by_xpath_or_default('//span[text()="단골"]/following-sibling::button[@disabled]', '0')

#이미지 추출
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
            except Exception as e:
                print(f"Error getting image URLs: {e}")
                break
        return list(image_urls)

urls = get_image_urls()
# 추출한 정보 출력
print(f"제목: {title}")
print(f"가격: {price}")
print(f"작성 시간: {post_time}")
print(f"조회수: {views}")
print(f"채팅수: {chats}")
print(f"찜수: {favorites}")
print(f"제품 상태: {product_condition}")
print(f"거래 방식: {transaction_method}")
print(f"배송비 포함 여부: {shipping_included}")
print(f"안전 거래 사용 여부: {safe_transaction}")
print(f"상품 정보: {product_info}")
print(f"판매자 ID: {seller_id}")
print(f"판매자 닉네임: {seller_nickname}")
print(f"신뢰지수: {trust_score}")
print(f"안전 거래 횟수: {safe_transaction_count}")
print(f"거래 후기 수: {reviews_count}")
print(f"단골 수: {loyal_customers_count}")
print(urls)

# 웹 드라이버 종료
driver.quit()