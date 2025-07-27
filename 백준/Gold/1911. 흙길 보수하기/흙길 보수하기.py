import sys 
input = sys.stdin.readline
from collections import deque

# 구하는 것: 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수
# 그리디
n, l = map(int, input().split())

puddle = []
for _ in range(n):
    start, end = map(int, input().split())
    puddle.append((start, end))

puddle.sort(key=lambda x:(-x[1]))
count = 0
prev_start = 1000000000
left = 0 # 남은 널빤지  길이

for start, end in puddle:
    # 남은 널빤지를 통해 이전 웅덩이와 연결된다면 남은 거 사용
    if end >= prev_start - left:
        end = max(start, prev_start - left)

    if end > start:
        length = end - start
        need = (length + l - 1) // l
        count += need
        prev_start = start
        left = need*l - length

print(count)