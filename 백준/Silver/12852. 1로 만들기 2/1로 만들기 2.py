import sys
input = sys.stdin.readline

n = int(input())

d = [0]*(n+1) # 연산횟수 초기화
ways = [0]*(n+1) # 이전 수 기록 배열 초기화

for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    ways[i] = i - 1

    # 현재의 수가 2으로 나누어 떨어지는 경우
    if i % 2 == 0:
        tmp = d[i//2] + 1
        d[i] = min(d[i], d[i//2] + 1)
        if d[i] == tmp:
            ways[i] = i//2

    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        tmp = d[i//3] + 1
        d[i] = min(d[i], d[i//3] + 1)
        if d[i] == tmp:
            ways[i] = i//3

result = []
cur = n
while True:
    result.append(cur)
    if cur == 1:
        break
    cur = ways[cur]

print(d[n])
print(*result)