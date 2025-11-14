import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

ans = E
while True:
    if (ans - S) % 28 == 0 and (ans - M) % 19 == 0:
        print(ans)
        break
    ans += 15