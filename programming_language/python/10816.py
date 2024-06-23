import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

# #딕셔너리를 통해 저장(키: 숫자,값: 숫자가 나온 횟수)
# #딕셔너리의 키값만을 리스트로 저장
N = int(input())
card1 =list(map(int, input().split()))
card1.sort()
card1_dictionary = dict()
for i in card1:
    if i in card1_dictionary: #있으면
        card1_dictionary[i] += 1
    else:#없으면
        card1_dictionary[i] = 1
card1_key_list = list(card1_dictionary.keys())



M = int(input())
card2 = list(map(int, input().split()))


# #그 리스트에 있는지 확인
# #없으면 0출력
# #있으면 딕셔너리 키값대입을 통해 값을 출력
for i in card2:
    if binary_search(card1, i, 0, N-1) != None:
        print(card1_dictionary[i], end=" ")
    else:
        print(0, end=" ")