def solution():
    n = int(input().strip())
    distance = list(map(int, input().strip().split()))
    price = list(map(int, input().strip().split()))

    ans = 0
    cheapest = float('inf')

    for i in range(n-1):
        if price[i] < cheapest:
            cheapest = price[i]
        ans += cheapest * distance[i]

    print(ans)

solution()