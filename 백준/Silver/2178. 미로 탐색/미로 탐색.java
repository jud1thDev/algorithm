import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 미로 저장
        int[][] maze = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                maze[i][j] = Integer.parseInt(String.valueOf(line.charAt(j)));
            }
        }

        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][M];

        // 이동 방향 {상, 하, 좌, 우}
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        q.add(new int[]{0, 0}); // 시작점 큐에 추가
        visited[0][0] = true;

        int min = 1; // 시작 칸도 포함

        while (!q.isEmpty()) {
            int size = q.size(); // 현재 레벨의 노드 수를 고정
            for (int s = 0; s < size; s++) {
                int[] cur = q.poll();
                int x = cur[0];
                int y = cur[1];

                // 도착지점이면
                if (x == N - 1 && y == M - 1) {
                    System.out.print(min);
                    return; // 즉시 종료
                }

                for (int i = 0; i < 4; i++) { // 상하좌우 4방향 탐색
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (nx >= 0 && ny >= 0 && nx < N && ny < M && maze[nx][ny] == 1 && !visited[nx][ny]) {
                        q.add(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
            min++; 
        }
    }
}
