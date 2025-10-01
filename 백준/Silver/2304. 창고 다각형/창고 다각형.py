import sys
input = sys.stdin.readline

# 구하는 것: 창고 다각형의 면적이 가장 작은 창고
# 아이디어: 가장 높은 기둥을 기준으로 왼쪽, 오른쪽으로 나누어 생각
n = int(input())
arr = []
for _ in range(n):
    l, h = map(int, input().split())
    arr.append((l, h))

arr.sort(key=lambda x: x[0]) # 위치 기준 정렬
max_h = max(h for _, h in arr)  

left_max_idx = None
right_max_idx = None
for i in range(n):
    if arr[i][1] == max_h:
        if left_max_idx is None:
            left_max_idx = i  
        right_max_idx = i

area = 0

# 왼쪽
cur_h = arr[0][1]
for i in range(left_max_idx):
    if arr[i][1] > cur_h:
        cur_h = arr[i][1]
    area += cur_h * (arr[i+1][0] - arr[i][0])

# 오른쪽
cur_h = arr[-1][1]
for i in range(n-1, right_max_idx, -1):
    if arr[i][1] > cur_h:
        cur_h = arr[i][1]
    area += cur_h * (arr[i][0] - arr[i-1][0])

area += (arr[right_max_idx][0] - arr[left_max_idx][0] + 1) * max_h

print(area)