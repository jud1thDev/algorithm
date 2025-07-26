def solution(cap, n, deliveries, pickups):
    answer = 0

    deliver_idx = n - 1
    pickup_idx = n - 1

    while deliver_idx >= 0 or pickup_idx >= 0:
        # 배달 끝난 집은 인덱스 줄이기
        while deliver_idx >= 0 and deliveries[deliver_idx] == 0:
            deliver_idx -= 1
        # 수거 끝난 집은 인덱스 줄이기
        while pickup_idx >= 0 and pickups[pickup_idx] == 0:
            pickup_idx -= 1
        
        # 모두 처리했으면 끝
        if deliver_idx < 0 and pickup_idx < 0:
            break
        
        # 가장 멀리 가야 하는 집까지 거리 계산
        furthest = max(deliver_idx, pickup_idx) + 1
        answer += furthest * 2  # 왕복 거리 더하기

        deliver_cap = cap
        pickup_cap = cap

        # 배달 처리
        while deliver_idx >= 0 and deliver_cap > 0:
            if deliveries[deliver_idx] <= deliver_cap:
                deliver_cap -= deliveries[deliver_idx]
                deliveries[deliver_idx] = 0
                deliver_idx -= 1
            else:
                deliveries[deliver_idx] -= deliver_cap
                deliver_cap = 0
        
        # 수거 처리
        while pickup_idx >= 0 and pickup_cap > 0:
            if pickups[pickup_idx] <= pickup_cap:
                pickup_cap -= pickups[pickup_idx]
                pickups[pickup_idx] = 0
                pickup_idx -= 1
            else:
                pickups[pickup_idx] -= pickup_cap
                pickup_cap = 0

    return answer
