def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_load = 0  # 누적 배달 물량
    pickup_load = 0   # 누적 수거 물량
    furthest_pos = n - 1  # 현재 왕복 시 가장 먼 집 위치

    for i in range(n - 1, -1, -1):
        deliver_load += deliveries[i]
        pickup_load += pickups[i]

        # 누적된 물량이 트럭 용량 초과하면 왕복 처리
        while deliver_load > cap or pickup_load > cap:
            answer += 2 * (furthest_pos + 1)  # 왕복 거리 누적
            deliver_load -= cap
            pickup_load -= cap
            furthest_pos = i  # 가장 먼 집 위치 갱신

    # 남은 물량 있으면 마지막 왕복 거리 더함
    if deliver_load > 0 or pickup_load > 0:
        answer += 2 * (furthest_pos + 1)

    return answer
