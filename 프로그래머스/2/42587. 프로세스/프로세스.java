import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> waiting = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            waiting.offer(new int[]{i, priorities[i]});
        }
        
        int count = 0;
        
        while (true) {
            int[] current = waiting.poll();
            
            if (waiting.stream().anyMatch(p -> p[1] > current[1])) {
                waiting.offer(current);
            } else {
                count++;
                if (current[0] == location) {
                    return count;
                }
            }
        }
    }
}
