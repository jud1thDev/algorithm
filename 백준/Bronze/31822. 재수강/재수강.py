import sys
input = sys.stdin.readline

target = input().strip()     
prefix = target[:5]  
N = int(input())

count = 0
for _ in range(N):
    code = input().strip()
    if code[:5] == prefix:
        count += 1

print(count)
