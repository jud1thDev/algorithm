import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<List<Integer>> graph = new ArrayList<>();

        // 입력
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        for (int i = 0; i <= n; i++){
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i< m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for (int i = 1; i <= n; i++){
            Collections.sort(graph.get(i));
        }

        boolean[] visited = new boolean[n+1];
        dfs(graph, visited, v);
        System.out.println();
        visited = new boolean[n+1];
        bfs(graph, visited, v);
    }

    static void dfs(List<List<Integer>> graph, boolean[] visited, int v){
        visited[v] = true;
        System.out.print(v + " ");
        for (int i : graph.get(v)){
            if (!visited[i]){
                dfs(graph, visited, i);
            }
        }
    }

    static void bfs(List<List<Integer>> graph, boolean[] visited, int v){
        Queue<Integer> q = new LinkedList<>();
        q.add(v);
        visited[v] = true;

        while (!q.isEmpty()){
            int cur = q.poll();
            System.out.print(cur + " ");
            for (int i : graph.get(cur)){
                if (!visited[i]){
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}