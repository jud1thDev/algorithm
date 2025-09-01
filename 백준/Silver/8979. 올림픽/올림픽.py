import sys
input = sys.stdin.readline

# 구하는 것: 입력받은 국가 K의 등수(정수)
n, k = map(int, input().split())

medals = []
for _ in range(n):
    country, gold, silver, bronze = map(int, input().split())
    medals.append((country, gold, silver, bronze))
    if country == k:
        target = (country, gold, silver, bronze)

medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
for country in medals:
    if (country[1], country[2], country[3]) > (target[1], target[2], target[3]):
        rank += 1

print(rank)
