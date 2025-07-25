import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

# M 이상 길이 단어만 필터링
filtered = [w for w in words if len(w) >= M]

# 단어 빈도 계산
from collections import Counter
count = Counter(filtered)

# 중복 제거한 단어 리스트
unique_words = list(count.keys())

# 정렬 (빈도 내림차순, 길이 내림차순, 사전순 오름차순)
unique_words.sort(key=lambda w: (-count[w], -len(w), w))

for w in unique_words:
    print(w)