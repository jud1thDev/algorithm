import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

base = Counter(words[0])
ans = 0

for i in range(1, n):
    cur = Counter(words[i])
    diff = 0

    for ch in set(base.keys()) | set(cur.keys()):
        diff += abs(base[ch] - cur[ch])

    if diff == 0:
        ans += 1
    elif diff == 1:
        ans += 1
    elif diff == 2 and len(words[0]) == len(words[i]):
        ans += 1

print(ans)
