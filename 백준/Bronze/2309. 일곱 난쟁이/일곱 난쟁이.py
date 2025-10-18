import sys
input = sys.stdin.readline

heights = [int(input()) for _ in range(9)]
over_height = sum(heights) - 100

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if heights[i] + heights[j] == over_height:
            heights.remove(heights[i])
            heights.remove(heights[j - 1]) # 첫 remove로 인덱스 한 칸 당겨짐
            heights.sort()
            print(*heights)
            found = True
            break
    if found: break