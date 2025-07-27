import sys 
input = sys.stdin.readline

# 구하는 것: 최대로 벌 수 있는 돈 
# 그리디 + 정렬
n = int(input())

offers = []
for _ in range(n):
    line = list(map(int, input().split()))
    offers.append(line) # 튜플 (p, d)

# 정렬: p 기준 내림차순
offers.sort(key=lambda x: (-x[0]))

# 강연 확정된 일 체크용 리스트
days = [False]*10001

ans = 0

for p, d in offers:
    for day in range(d, 0, -1):
        if not days[day]:
            days[day] = True
            ans += p
            break

print(ans)