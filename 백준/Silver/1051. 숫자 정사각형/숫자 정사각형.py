import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 정답 정사각형의 크기
def solution():
    n, m = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(n)] # n행 m열
    ans = 1 # 기본값

    for size in range(min(n,m), 1, -1):
        found = False
        for i in range(n-size+1):
            for j in range(m-size+1):
                top_left = arr[i][j]
                top_right = arr[i][j+size-1]
                bottom_left = arr[i+size-1][j]
                bottom_right = arr[i+size-1][j+size-1]

                if top_left == top_right == bottom_left == bottom_right:
                    ans = size*size
                    found = True
                    break
            if found: break
        if found: break
        
    return print(ans)

solution()