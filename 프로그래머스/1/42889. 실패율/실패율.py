def solution(N, stages):
    count = [0] * (N + 2) # 인덱스에러 방지용 N+1 +1 해줌
    for stage in stages:
        count[stage] += 1
    
    total_users = len(stages)
    fail_rates = []
    
    for stage in range(1, N+1):
        if total_users == 0:
            fail_rate = 0
        else:
            fail_rate = count[stage] / total_users
        fail_rates.append((stage, fail_rate))
        total_users -= count[stage]
        
    # 정렬: 실패율 내림차순, 스테이지 번호 오름차순
    fail_rates.sort(key=lambda x:(-x[1], x[0]))
    return [f[0] for f in fail_rates]
    