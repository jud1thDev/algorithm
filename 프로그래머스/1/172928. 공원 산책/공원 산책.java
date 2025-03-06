import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] position = new int[2];

        // 1. 강아지 시작 위치 찾기 : park 배열 순회
        for (int i = 0; i < park.length; i++) { // 공원의 세로
            for (int j = 0; j < park[0].length(); j++) { // 공원의 가로
                if (park[i].charAt(j) == 'S') {
                    position[0] = i;
                    position[1] = j;
                    break;
                }
            }
        }

        Map<String, int[]> directionMap = new HashMap<>();
        directionMap.put("E", new int[]{0, 1});
        directionMap.put("W", new int[]{0, -1});
        directionMap.put("S", new int[]{1, 0});
        directionMap.put("N", new int[]{-1, 0});

        // for문: route 순회하면서, if문: 주어진 제약 확인
        for (String route : routes) {
            String[] parts = route.split(" ");
            String dir = parts[0];
            int distance = Integer.parseInt(parts[1]);

            if (canMove(position, dir, distance, park, directionMap)) {
                position[0] += directionMap.get(dir)[0] * distance;
                position[1] += directionMap.get(dir)[1] * distance;
            }
        }
        return position;
    }

    private boolean canMove(int[] position, String dir, int distance, String[] park, Map<String, int[]> directionMap) {
        int[] move = directionMap.get(dir);
        int x = position[0];
        int y = position[1];

        for (int i = 1; i <= distance; i++) {
            int newX = x + move[0] * i;
            int newY = y + move[1] * i;

            if (newX < 0 || newX >= park.length || newY < 0 || newY >= park[0].length()) {
                return false; // 범위를 벗어나면 이동 불가
            }
            if (park[newX].charAt(newY) == 'X') {
                return false; // 장애물이 있으면 이동 불가
            }
        }
        return true;
    }
}
