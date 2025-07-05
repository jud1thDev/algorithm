import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 가장 많이 담긴 바구니와 적게 담긴 바구니의 공 개수 차이 최소값
def solution():
    n, k = map(int, input().split())

    ans = -1
    necessary = 0
    tmp = 0

    for i in range(k):
        tmp += 1
        necessary += tmp
    
    left = n - necessary

    if left >= 0:
        if left % k == 0:
            ans = k - 1
        else: ans = k

    return print(ans)
    
solution()