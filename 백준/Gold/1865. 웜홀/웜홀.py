import sys
input = sys.stdin.readline

# 구하는 것: TC개의 줄에 걸쳐서 출발 위치로 돌아오는 것이 가능하면 YES
TC = int(input().strip())

for _ in range(TC):
    N, M, W = map(int, input().strip().split())
    lines = []

    for _ in range(M):
        S, E, T = map(int, input().strip().split())
        lines.append((S, E, T))
        lines.append((E, S, T)) # 도로는 양방향

    for _ in range(M+2, M+W+2):
        s, e, t= map(int, input().strip().split())
        lines.append((s, e, -t))

    value = [0] * (N+1)
    ans = "NO" # 기본값
    for i in range(N):
        for S, E, T in lines:
            if value[E] > value[S] + T:
                value[E] = value[S] + T
                if i == N-1: ans = "YES"
            
    print(ans)