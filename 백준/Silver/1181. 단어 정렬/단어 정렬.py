import sys
input = sys.stdin.readline

N = int(input().strip())

words = set()
for _ in range(N):
    line = input().strip()
    words.add(line)

words = list(words)
words.sort(key=lambda x: (len(x), x))
for w in words:
    print(w)
