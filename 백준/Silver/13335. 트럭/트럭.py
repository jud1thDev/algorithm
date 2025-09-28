import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
waiting = deque(map(int, input().split()))

bridge = deque([0] * w) 
time = 0
cur = 0  

while waiting or cur > 0:
    time += 1
    cur -= bridge.popleft() 

    if waiting and cur + waiting[0] <= L:
        t = waiting.popleft()
        bridge.append(t)
        cur += t
    else:
        bridge.append(0)

print(time)
