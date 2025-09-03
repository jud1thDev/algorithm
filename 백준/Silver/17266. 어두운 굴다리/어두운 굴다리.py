import sys
input = sys.stdin.readline

# 구하는 것: 굴다리 길이 N을 모두 비추기 위한 가로등의 최소 높이

N = int(input())
M = int(input())
streetlamps = list(map(int, input().split()))

def binary_search(start, end, answer):
    if start > end: 
        return answer
    mid = (start + end) // 2

    current = 0
    possible = True
    for lamp in streetlamps:
        if lamp - mid > current:
            possible = False
            break
        current = max(current, lamp + mid)
    if current < N:
        possible = False
    if possible:
        return binary_search(start, mid -1, mid)
    else:
        return binary_search(mid + 1, end, answer)
    
result = binary_search(0, N, N)
print(result)