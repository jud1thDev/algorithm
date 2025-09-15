import sys
input = sys.stdin.readline

# 구하는 것: 필요한 교환의 회수의 최솟값
given = input().strip()

a = given.count('a')
double = given * 2
b = double[:a].count('b')
ans = b # 초기값 세팅

for i in range(1, len(given)):
    if double[i - 1] == 'b':
        b -= 1
    if double[i + a - 1] == 'b':
        b += 1
    ans = min(ans, b)

print(ans)