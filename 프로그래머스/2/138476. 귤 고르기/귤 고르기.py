from collections import Counter

# 구하는 것: 귤을 크기별로 분류했을 때 서로 다른 종류의 최솟값
def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_count = sorted(count.values(), reverse=True)
    
    # 출력값 구하기
    ans = 0
    for i in sorted_count:
        if k > 0:
            ans += 1
            k -= i
            
    return ans
    
    