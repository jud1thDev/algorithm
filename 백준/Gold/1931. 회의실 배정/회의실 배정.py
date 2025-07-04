import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 최대 사용할 수 있는 회의 개수
def solution():
    n = int(input().strip())
    meeting = []
    ans = 0

    for _ in range(n):
        start, end = map(int, input().strip().split())
        meeting.append((start, end))
    
    # 종료 시간 오름차순 정렬
    meeting.sort(key=lambda x: (x[1], x[0]))

    meeting_end = 0
    for s, e in meeting:
        if s >= meeting_end:
            ans += 1
            meeting_end = e
    
    return print(ans)
    
solution()