# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())

# result_dict = {}

# for i in range(N):
#     word = input()
#     if len(word) >= M:
#         if word in result_dict:
#             result_dict[word] += 1
#         else:
#             result_dict[word] =1 #입력받고 빈도 랑 저장
    
#     #빈도 대로 묶기
#     frequency = list(result_dict.values())
#     frequency.sort(reverse=True)

#     frequncy_list= [0] * len(frequency)
#     for i in frequency: #가장 높은순서대로 그룹화
#         for j in result_dict:
#             if i == j:
#                 frequency_list

#선생님풀이:

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

count_dict = {}
for _ in range(N):
    word = input().rstrip()
    if len(word)<M:continue
    count_dict[word] = count_dict.get(word,0)+1 #빈도수체크임 기억하셈

ordered_dict={}
for _k,v in count_dict.items():
    if v not in ordered_dict:
        ordered_dict[v] = {}
    length = len(k)

    if length not in ordered_dict[v]:
        ordered_dict[v][length]=[]
    ordered_dict[v][length].append(k)

for k1 in sorted(ordered_dict, reverse=True):
    for k2 in sorted(ordered_dict[k1], reverse=True):
        for word in sorted(ordered_dict[k1][k2]):
            print(word)
            print(word)