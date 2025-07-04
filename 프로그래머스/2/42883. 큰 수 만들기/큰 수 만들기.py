# 구하는 것: number에서 k 개의 수를 제거했을 때 만들 수 있는 가장 큰 숫자
def solution(number, k):
    
    stack = []
    remove_cnt =0
    
    for n in number: # 문자열에서 한글자씩 꺼내기
        # 스택에 숫자가 있고, 현재 숫자가 스택top보다 크고, remove_cnt가 남아있음
        while stack and remove_cnt < k and n > stack[-1]:
            stack.pop()
            remove_cnt += 1
        stack.append(n)
    
    # k만큼 remove_cnt 못한 경우
    if remove_cnt < k:
        stack = stack[:-k+remove_cnt]
    
    return ''.join(stack)