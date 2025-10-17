import sys
input = sys.stdin.readline

n = int(input().strip())
people = [tuple(map(int, input().split())) for _ in range(n)]

ranks = []
for i in range(n):
    w_i, h_i = people[i]
    bigger = 0
    for j in range(n):
        if i == j:
            continue
        w_j, h_j = people[j]
        if w_j > w_i and h_j > h_i:
            bigger += 1
    ranks.append(bigger + 1)

print(*ranks)