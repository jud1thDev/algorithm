# 구하는 것: 모든 차량이 카메라를 만나도록 하는 최소 카메라 개수
def solution(routes):
    routes.sort(key=lambda x: x[1])
    ans = 0
    camera = -30001
    
    for s, e in routes:
        if camera < s :
            camera = e
            ans += 1
            
    return ans