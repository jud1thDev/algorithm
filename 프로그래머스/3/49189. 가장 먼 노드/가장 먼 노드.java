import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        // 1. 인접 리스트를 만들고
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++){
            graph.add(new ArrayList<>());
        }
        
        // 2. 간선을 인접 리스트에 추가
        for (int[] vertex : edge) {
            int a = vertex[0];
            int b = vertex[1];
            graph.get(a).add(b); // 양방향 이므로 {a, b}
            graph.get(b).add(a); // {b, a} 둘 다 추가 
        }
        
        // 3. BFS로 최단 거리 찾기
        Queue<Integer> queue = new LinkedList<>();
        int[] distance = new int[n + 1]; // 최단거리. 0번 인덱스 안 쓰려고 n+1. 
        Arrays.fill(distance, -1); // 모든 노드를 방문 전 -1로 초기화
        queue.add(1); // 탐색 시작: 1번 노드를 큐에 추가
        distance[1] = 0; // 1번 노에서 자기 자신까지 거리는 0
        
        while (!queue.isEmpty()){ 
            int current = queue.poll(); // 큐 맨앞에 있는 애 하나 꺼내
            for (int next : graph.get(current)){ // 현재 노드와 관련된 모든 노드를 가져옴
                if (distance[next] == -1){ // -1이면 방문하지 않은 노드
                    distance[next] = distance[current] + 1; // next는 current에서 이동한 것이므로, 거리를 1 증가시킴.
                    queue.add(next);
                }
            }
        }
        
        int max = 0; // 가장 멀리 떨어진 거리
        int count = 0; // 가장 멀리 떨어진 노드 개수
        for (int i = 1; i <= n; i++){
            if (distance[i] > max){
                max = distance[i];
                count = 1; // 이전 count값 초기화
            } else if (distance[i] == max) count++;
        }
        return count;
    }
}