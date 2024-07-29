import requests
from bs4 import BeautifulSoup

# 크롤링할 URL
url = 'https://web.joongna.com/product/177825786'

# HTTP GET 요청
response = requests.get(url)
response.raise_for_status()  # 요청 실패 시 에러 발생

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 요소 추출 함수
def get_text_or_default(selector, default=''):
    element = soup.select_one(selector)
    return element.get_text(strip=True) if element else default

def get_text_or_default_nth(selector, index, default=''):
    elements = soup.select(selector)
    return elements[index].get_text(strip=True) if len(elements) > index else default

def get_attribute_or_default(selector, attribute, default=''):
    element = soup.select_one(selector)
    return element[attribute] if element and attribute in element.attrs else default

# 제목 추출
title = get_text_or_default('h1.text-lg.font-semibold, h1.md\\:text-2xl')

# 가격 추출
price = get_text_or_default('div.font-bold.md\\:text-\\[32px\\]')

# 작성 시간 추출
post_time_full = get_text_or_default('span.text-jnGray-500.leading-\\[15px\\]')
post_time = post_time_full.split('·')[0].strip() if post_time_full else ''

# 제품 상태 추출
product_condition = get_text_or_default_nth('button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1', 0)

# 거래 방식 추출
transaction_method = get_text_or_default_nth('button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1', 1)

# 배송비 포함 여부 추출
shipping_included = get_text_or_default_nth('button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1', 2)

# 안전 거래 사용 여부 추출
safe_transaction = get_text_or_default_nth('button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1', 3)

# 상품 정보 추출
product_info = get_text_or_default('p.flex-1.py-5.text-base.font-normal.break-words.break-all.whitespace-pre-line.text-jnGray-900')

# 판매자 정보 추출 (ID, 닉네임)
seller_info = soup.select_one('a.flex.items-center.justify-between.w-full.pt-5.lg\\:pt-\\[28px\\].lg\\:pb-5')
if seller_info:
    seller_id = seller_info['href']
    seller_nickname = seller_info.select_one('p.text-\\[22px\\]').get_text(strip=True)
else:
    seller_id = ''
    seller_nickname = ''

# 신뢰지수 추출
trust_score = get_text_or_default('span.ml-1.text-lg.font-semibold')

# 안전 거래 횟수 추출
safe_transaction_count = get_text_or_default('button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1:nth-of-type(2)')

# 거래 후기 수 추출
reviews_count = get_text_or_default('button.block.text-sm.font-semibold.text-jnblack.mt-1.underline')

# 단골 수 추출
loyal_customers_count = get_text_or_default('button:disabled.block.text-sm.font-semibold.text-jnblack.mt-1:nth-of-type(3)')

# 추출한 정보 출력
print(f"제목: {title}")
print(f"가격: {price}")
print(f"작성 시간: {post_time}")
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
