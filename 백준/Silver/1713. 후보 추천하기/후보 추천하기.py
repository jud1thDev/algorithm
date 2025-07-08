import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력
def solution():
    n = int(input()) # 사진틀 개수
    m = int(input()) # 추천 학생 수
    recommends = list(map(int, input().split()))

    frames = [] # [(학생번호, 추천횟수, 등록순서), ..]
    time = 0 # 등록순서 체크용

    for student in recommends:
        time += 1
        found = False

        for i in range(len(frames)):
            if frames[i][0] == student: # 똑같은 학생번호가 있으면
                frames[i] = (frames[i][0], frames[i][1]+1, frames[i][2]) # 추천횟수만 +1
                found = True
                break
        
        if not found:
            if len(frames) == n: # 사진틀이 꽉 참
                frames.sort(key=lambda x: (x[1], x[2])) # 추천횟수, 등록순서 오름차순
                frames.pop(0)
            frames.append((student, 1, time)) 
    
    ans = sorted([f[0] for f in frames])

    return print(*ans)

solution()
