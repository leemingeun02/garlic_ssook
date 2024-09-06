import sys
input = sys.stdin.readline
from collections import deque

P = int(input())

for _ in range(P):
    first_number, lines = input().split(" ", 1)
    first_number = int(first_number) - 1  # 인덱스로 변환
    lines = list(map(int, lines.split(" ")))
    
    # 첫 번째 학생을 대기열에 추가
    queue = [lines[first_number]]
    total_moves = 0

    # 나머지 학생들을 처리
    for i in range(len(lines)):
        if i == first_number:
            continue
        
        student_height = lines[i]
        if student_height <= queue[-1]:
            queue.append(student_height)
        else:
            # 대기열에서 학생을 찾고 삽입 위치를 결정
            for j in range(len(queue)):
                if student_height < queue[j]:
                    queue.insert(j, student_height)
                    total_moves += len(queue) - j - 1
                    break

    print(total_moves)
