def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]> target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)



N = int(input())
card1 =list(map(int, input().split()))
card1.sort()
M = int(input())
card2 = list(map(int, input().split()))

for i in card2:
    if binary_search(card1, i, 0, N-1) != None:
        print(1)
    else:
        print(0)
