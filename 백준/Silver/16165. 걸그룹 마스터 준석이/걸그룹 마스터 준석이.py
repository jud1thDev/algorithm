import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 걸그룹 수, 문제 수
g2m = {}
m2g = {}

# 걸그룹 정보 입력
for _ in range(N):
    team = input().strip()
    k = int(input().strip())
    members = []
    for _ in range(k):
        name = input().strip()
        members.append(name)
        m2g[name] = team
    members.sort()
    g2m[team] = members

# 퀴즈 처리
for _ in range(M):
    q = input().strip()
    t = int(input().strip())
    if t == 0:
        for name in g2m[q]:
            print(name)
    else:
        print(m2g[q])