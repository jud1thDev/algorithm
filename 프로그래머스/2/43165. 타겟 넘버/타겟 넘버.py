def solution(numbers, target):
    count = 0
    
    def dfs(index, total):
        nonlocal count
        # 종료: 모든 숫자를 다 사용함
        if index == len(numbers):
            if total == target:
                count += 1
            return
        
        # 재귀 실행
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])
    
    dfs(0, 0)
    return count
