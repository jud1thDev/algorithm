import sys
input = sys.stdin.readline

# 태그 안/밖 상태 분리, 태그 밖에서만 단어를 뒤집기
S = input().strip()
result = []
buf = []
i = 0
n = len(S)

while i < n:
    if S[i] == '<':
        # < 만나면 지금까지 모은 단어 뒤집어 출력
        if buf:
            result.extend(reversed(buf))
            buf.clear()
        # 태그 안은 그대로 출력
        while i < n:
            result.append(S[i])
            if S[i] == '>':
                i += 1
                break
            i += 1
    elif S[i] == ' ':
        if buf:
            result.extend(reversed(buf))
            buf.clear()
        result.append(' ')
        i += 1
    else: 
        buf.append(S[i])
        i += 1

if buf:
    result.extend(reversed(buf))

print(''.join(result))