import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 스위치 20개씩 배열
def solution():
    n = int(input()) # 스위치수
    switches = list(map(int, input().split()))
    m = int(input()) # 학생수

    arr = [list(map(int, input().split())) for _ in range(m)] # [성별, 받은번호]

    for gender, given in arr:
        if gender == 1: # 남자
            for i in range(given-1, n, given):
                switches[i] = change_switch(switches[i])

        elif gender ==2: # 여자 
            check = given -1 
            switches[check] = change_switch(switches[check]) # 중심 스위치 상태 변경
            left = check - 1
            right = check + 1
            while left >= 0 and right < n and switches[left] == switches[right]:
                switches[left] = change_switch(switches[left])
                switches[right] = change_switch(switches[right])
                left -= 1
                right += 1

    results = []

    # 출력: 20개씩 줄바꿈
    for i in range(0, len(switches), 20):
        results.append(' '.join(map(str, switches[i:i+20])))

    return print('\n'.join(results))

def change_switch(status):
    changed_status = status
    if status == 1:
        changed_status = 0
    else: changed_status = 1
    return changed_status

solution()
