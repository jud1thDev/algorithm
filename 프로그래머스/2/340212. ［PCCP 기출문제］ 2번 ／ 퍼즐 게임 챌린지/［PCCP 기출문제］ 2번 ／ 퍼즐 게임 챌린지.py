def solution(diffs, times, limit):
    # 현재 숙련도로 퍼즐을 제한 시간 내에 해결할 수 있는지 확인하는 함수
    def can_solve(level):
        clear_time = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:  # 난이도가 숙련도 이하이면 단순히 소요 시간만 더함
                clear_time += times[i]
            else:
                # 틀리는 횟수 계산
                mistakes = diffs[i] - level
                # 틀릴 때 걸리는 시간 계산 (현재 퍼즐 시간 + 이전 퍼즐 시간)
                clear_time += (times[i] + (times[i - 1] if i > 0 else 0)) * mistakes
                # 다시 해결하는 데 걸리는 시간 추가
                clear_time += times[i]
            # 제한 시간 초과 시 False 반환
            if clear_time > limit:
                return False
        return True

    # 이진 탐색으로 최소 숙련도를 찾음
    left, right = 1, max(diffs)
    answer = right  # 초기 답을 최대 난이도로 설정
    while left <= right:
        mid = (left + right) // 2  # 중간값 계산
        if can_solve(mid):  # 현재 중간 숙련도로 해결 가능하면
            answer = mid  # 답을 업데이트
            right = mid - 1  # 더 낮은 숙련도를 탐색
        else:
            left = mid + 1  # 더 높은 숙련도를 탐색
    return answer  # 최소 숙련도를 반환
