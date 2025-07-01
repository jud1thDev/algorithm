def solution():
    expression = input().strip()
    
    # - 기준으로 나눔
    parts = expression.split('-')
    
    # 첫 번째 파트는 그냥 더함
    total = sum(map(int, parts[0].split('+')))
    
    # 두 번째 파트부터는 괄호 안에 묶여 있다고 생각하고 전부 더해서 뺌
    for part in parts[1:]:
        total -= sum(map(int, part.split('+')))
    
    print(total)

solution()
