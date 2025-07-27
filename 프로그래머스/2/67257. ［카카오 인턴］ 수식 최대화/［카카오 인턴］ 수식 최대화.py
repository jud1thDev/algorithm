import re

# 구하는 것: 우승 시 받을 수 있는 가장 큰 상금 금액 
# dfs
def solution(expression):
    splited = re.split(r'([-+*])', expression)
    ops = list(set([i for i in splited if i in '-+*'])) # 주어진 연산자 중복없이 추출
    answer = 0
    
    def calculate(priority):
        expr = splited[:]
        for op in priority:
            # 연산자 op가 있는 동안 계속 계산
            while op in expr:
                idx = expr.index(op)
                a = int(expr[idx - 1])
                b = int(expr[idx + 1])
                if op == '+':
                    result = a + b
                elif op == '-':
                    result = a - b
                elif op == '*':
                    result = a * b
                # 계산한 결과로 3개 자리를 1개로 바꿈
                expr = expr[:idx - 1] + [str(result)] + expr[idx + 2:]
        return abs(int(expr[0])) # 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출
        
    used = [False]*len(ops)
    
    def dfs(idx, order):
        nonlocal answer
        if idx == len(ops):
            answer = max(answer, calculate(order))
            return
        for i in range(len(ops)):
            if not used[i]:
                used[i] = True
                dfs(idx + 1, order + [ops[i]])
                used[i] = False # 백트래킹
    dfs(0, [])
    return answer