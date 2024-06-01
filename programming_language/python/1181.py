def sort_words(words):
    # 중복을 제거하기 위해 set을 사용
    unique_words = set(words)
    
    # 단어를 정렬: 먼저 길이순으로, 그 다음 사전순으로
    sorted_words = sorted(unique_words, key=lambda word: (len(word), word))
    
    return sorted_words

# 입력
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# 정렬된 단어 리스트
sorted_words = sort_words(words)

# 결과 출력
for word in sorted_words:
    print(word)
