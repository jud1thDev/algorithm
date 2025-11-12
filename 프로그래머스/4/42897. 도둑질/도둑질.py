# 구하는 것: 도둑이 훔칠 수 있는 돈의 최댓값
def solution(money):
    n = len(money)

    # 인접한 두 집을 훔칠 수 없음
    # 첫 번쨰 집을 훔치는 경우
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
        max1 = dp1[i]
    
    # 첫 번째 집을 훔치지 않는 경우
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])
        max2 = dp2[i]
    
    return max(max1, max2)