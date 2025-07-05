# 통채우기 문제

# 구하는 것: 필요한 구명보트 개수의 최소값
def solution(people, limit):
    people.sort()
    cnt = 0
    left = 0
    right = len(people) -1
    
    while left <= right:
        if people[left] +people[right] <= limit:
            left += 1
        right -= 1
        cnt += 1
        
    return cnt