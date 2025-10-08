import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
count = {}
ans = 0
while right < n:
    count[arr[right]] = count.get(arr[right], 0) + 1 # arr[right] 추가
    while count[arr[right]] > k: # k 초과 시
        count[arr[left]] -= 1
        left += 1 # left 이동
    ans = max(ans, right - left + 1)
    right += 1 
print(ans)