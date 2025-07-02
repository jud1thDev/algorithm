# 일직선 노드 있는 것부터 그리디 느낌 

# 구하는 것: 왼쪽부터 오른쪽까지의 최소 비용
def solution():
    n = int(input().strip())
    distance = list(map(int, input().strip().split()))
    price = list(map(int, input().strip().split()))

    ans = 0
    left_distance = sum(distance)
    cheapest = float('inf')
    # 맨마지막 주유소는 의미없고, i-1번째까지 생각했을 때
    # 내 뒤에 젤 싼 주유소(cheapest)가 있으면 지금은 딱 당장 필요한 것만 주유하자
    # cheapest에서 그냥 다 충전
    for i in range(n-1):
        if price[i] < cheapest:
            cheapest = price[i]
    
    for i in range(len(distance)):
        if price[i] > cheapest:
            ans += price[i]*distance[i]
        else: 
            ans += price[i]*left_distance
            break
        left_distance -= distance[i]

    print(ans)

solution()
