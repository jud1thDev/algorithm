import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    m = int(input())
    recommends = list(map(int, input().split()))

    frames = []  # (학생번호, 추천수)

    for student in recommends:
        for i, (num, cnt) in enumerate(frames):
            if num == student:
                frames[i] = (num, cnt + 1)
                break
        else:
            if len(frames) < n:
                frames.append((student, 1))
            else:
                min_cnt = min(frames, key=lambda x: x[1])[1]
                for i, (num, cnt) in enumerate(frames):
                    if cnt == min_cnt:
                        frames.pop(i)
                        break
                frames.append((student, 1))

    answer = sorted(num for num, cnt in frames)
    print(*answer)

solution()
