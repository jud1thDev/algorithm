def solution(n, times):
    left = 1 # 최소시간
    right = max(times)*n # 최대시간
    
    while left <= right:
        mid = (left + right) // 2
        people = sum(mid // time for time in times)
        
        if people >= n: # mid시간 안에 사람 충분히 처리
            answer = mid 
            right = mid - 1
        else: left = mid + 1
        
    return answer