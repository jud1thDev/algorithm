import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prefix_set = set()

for _ in range(N):
    word = input().strip()
    for i in range(1, len(word) + 1):
        prefix_set.add(word[:i])


cnt = 0
for _ in range(M):
    checkword = input().strip()
    if checkword in prefix_set:
        cnt += 1

print(cnt)