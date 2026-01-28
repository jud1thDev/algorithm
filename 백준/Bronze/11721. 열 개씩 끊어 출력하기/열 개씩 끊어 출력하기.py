import sys
input = sys.stdin.readline

word = input().strip()
n = len(word)
for i in range(0, n, 10):
    print(word[i:i+10])