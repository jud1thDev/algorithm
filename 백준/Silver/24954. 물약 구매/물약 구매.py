import sys
input = sys.stdin.readline

n = int(input())
c = [0] + list(map(int, input().split())) # 0번 인덱스는 버림
sale = [[] for _ in range(n+1)]
for i in range(1, n+1):
    p = int(input())
    for _ in range(p):
        a, d = map(int, input().split())
        sale[i].append((a, d))

ans = float('inf')
visited = [False] * (n+1)

def dfs(depth, total):
    global ans
    if total >= ans:  # 가지치기
        return
    if depth == n: # 모든 물건 구매 완료
        ans = min(ans, total)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            # 할인 적용
            discounted = []
            for target, discount in sale[i]:
                if not visited[target]:
                    before = c[target]
                    c[target] = max(1, c[target] - discount)
                    discounted.append((target, before))
            dfs(depth+1, total + c[i])
            # 할인 복구
            for target, before in discounted:
                c[target] = before
            visited[i] = False

dfs(0, 0)
print(ans)