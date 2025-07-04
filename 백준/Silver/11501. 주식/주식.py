import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 테스트케이스별로 최대이익
def solution():

    t = int(input().strip())
    results = []

    for _ in range (t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        price = 0 # 팔 가격
        ans = 0
        
        for i in reversed(arr):
            if i > price:
                price = i
            ans += (price - i)
        results.append(ans)

    return print('\n'.join(map(str, results)))
    
solution()