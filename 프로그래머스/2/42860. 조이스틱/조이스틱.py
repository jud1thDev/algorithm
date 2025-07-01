def solution(name):
    
    cnt = 0
    for ch in name:
        # 다음/이전 알파벳 중 무엇이 빠를지
        diff = min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
        cnt += diff
    
    length = len(name)
    cursor = length - 1 # 오른쪽으로만 이동(기본 최소값)
    
    for i in range(length):
        next = i + 1
        # A 스킵
        while next < length and name[next] == 'A':
            next += 1 # next는 A가 끝나는 위치
        # 최소 커서 이동 횟수 결정
        # 오른쪽으로 이동 + A 스킵 후 바꿔야할 문자가 있는 곳부터 오른쪽 끝까지 남은 거리 + 돌아갈 때 짧은 쪽
        cursor = min(cursor, i + (length - next) + min(i, length - next)) 
        
    cnt += cursor
    return cnt