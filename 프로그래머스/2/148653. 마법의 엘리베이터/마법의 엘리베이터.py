# 구하는 것: 0층으로 가기 위한 마법의 돌 최수 개수
def solution(storey): 
    ans = 0
    while storey:
        x = storey % 10 
        next = (storey // 10) % 10
        if x < 5: # 특정 자릿수의 값이 5 이하면 그냥 내림
            ans += x
        elif x > 5: # 특정 자릿수의 값이 5 이상이면 올림
            ans += 10 - x
            storey += 10 # 근데 다음 자릿수에 영향 줌 
        else: # 자릿수의 값이 5인 경우는 특이점
            if next >= 5: # 올림
                ans += 5
                storey += 10
            else: # 내림 
                ans += 5 
        storey //= 10
        
    return ans