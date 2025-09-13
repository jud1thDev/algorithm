import sys
input = sys.stdin.readline

# 구하는 것: 가장 인접한 두 공유기 사이의 최대 거리
n, c = map(int, input().split()) # 도현이가 집이 n개나 있다고? 좋겠다
x_list = [int(input()) for _ in range(n)]
x_list.sort()

def binarySerarch(x_list, c, left, right):
    if left > right:
        return right
    mid = (left + right) // 2

    # 설치 가능한지 확인
    cnt = 1
    last = x_list[0]
    for i in range(1, len(x_list)):
        if x_list[i] - last >= mid:
            cnt += 1
            last = x_list[i]
    
    if cnt >= c:
        return binarySerarch(x_list, c, mid + 1, right)
    else: return binarySerarch(x_list, c, left, mid - 1)

print(binarySerarch(x_list, c, 1, x_list[-1] - x_list[0]))