import sys
input = sys.stdin.readline

from collections import deque

# 구하는 것: 몇 번째 단계가 진행 중일때 종료되었는지
n, k = map(int, input().split())
a_list = deque(map(int, input().split()))
robots = deque([False] * n)

step = 0

while True:
    step += 1

    # 1
    a_list.rotate(1)
    robots.rotate(1)
    robots[-1] = False  

    # 2
    for i in range(n - 2, -1, -1):  
        if robots[i] and not robots[i + 1] and a_list[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            a_list[i + 1] -= 1
    robots[-1] = False  

    # 3
    if a_list[0] > 0:
        robots[0] = True
        a_list[0] -= 1

    # 4
    if a_list.count(0) >= k:
        break

print(step)