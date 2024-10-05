from openai import OpenAI

# OpenAI 클라이언트 초기화 시 API 키 전달
client = OpenAI(api_key="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")

# 챗 완료 요청
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "0을 99개 출력해."
        }
    ]
)

print(completion.choices[0].message)
