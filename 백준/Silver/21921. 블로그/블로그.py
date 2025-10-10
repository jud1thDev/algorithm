import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

# 슬라이딩윈도우
current_sum = sum(visitors[:x])
max_sum = current_sum
count = 1
for i in range(x, n):
    current_sum += visitors[i] - visitors[i - x]
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)