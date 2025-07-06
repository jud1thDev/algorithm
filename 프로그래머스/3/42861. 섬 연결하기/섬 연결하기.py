# 구하는 것: 모든 노드가 연결된 최소 비용
# MST인데 사이클 있어도 되는듯? 
def solution(n, costs):
    costs.sort(key=lambda x: x[2]) # 비용 기준 오름차순 정렬
    
    # 초기값 세팅
    connected = set([costs[0][0], costs[0][1]])
    ans = costs[0][2]
    cnt = 1
    
    while cnt < n-1: # 노드가 n개일 때 n-1개의 간선으로 해결 가능하니까
        for i in range(len(costs)):
            a, b, cost = costs[i] # 주어진 배열 분리
                
            # a연결b연결x 혹은 a연결xb연결o    
            if (a in connected or b in connected) and not (a in connected and b in connected):
                connected.add(a)
                connected.add(b)
                ans += cost
                cnt += 1
                costs.pop(i)
                break
        
    return ans