# 구하는 것: 체육 수업을 듣는 최대 학생수
def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # 여벌이 있는데 도난당해서 다른 학생에게 빌려줄 수 없는 경우 처리
    intersection = lost_set & reserve_set
    lost_set -= intersection 
    reserve_set -= intersection
    
    ans = n - len(lost_set) # 기본값

    for i in sorted(lost_set):
        for j in (i-1, i+1):
            if j in reserve_set:
                reserve_set.remove(j)
                ans += 1
                break
                
    return ans