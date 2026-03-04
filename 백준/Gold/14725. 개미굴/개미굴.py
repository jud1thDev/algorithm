import sys
input = sys.stdin.readline

N = int(input().strip()) #먹이의 정보 개수

paths = []

for _ in range(N):
    given = input().split()
    K = int(given[0])
    foods = given[1:]
    paths.append(foods)

paths.sort()
prev = []
for path in paths:
    i = 0
    while i < len(prev) and i < len(path) and prev[i] == path[i]:
        i += 1
    
    for j in range(i, len(path)):
        print("--" * j + path[j])

    prev = path
