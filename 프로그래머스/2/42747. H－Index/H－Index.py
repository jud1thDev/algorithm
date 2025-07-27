# 구하는 것 : h번 인용된 논문이 h번 이상일 때, h의 최댓값
def solution(citations):
    citations.sort(reverse=True)
    ans = 0
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            ans = i + 1
        else:
            break

    return ans