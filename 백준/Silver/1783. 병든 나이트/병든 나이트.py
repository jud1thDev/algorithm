import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 방문할 수 있는 최대 칸의 개수
def solution():
    n, m = map(int, input().split())

    if n == 1:
        ans = 1 # 위/아래로 이동 불가하므로 어떠한 이동도 불가능함, 처음위치만 카운트
    elif n == 2: # 위/아래로 1칸씩만 이동 가능
        ans = min(4, (m + 1) // 2) # 위/아래로 1칸씩만 이동 가능하므로 4가지 방법을 다 쓰는 건 불가능하므로 최대 3칸의 방문만 허용된다
    else: 
        # 이동 4번 이상 하려면 오른쪽으로 최소 7칸이 있어야 함(1~4번 방법의 오른쪽 이동을 전부 더함 + 처음 위치 1칸= 1+2+2+1)
        if m >= 7:
            ans = m - 2 # 이동방법 제약때문에 2번은 오른쪽 1칸 움직이는 걸 사용해야 하기 때문
        else: ans = min(4, m)

    return print(ans)

solution()
