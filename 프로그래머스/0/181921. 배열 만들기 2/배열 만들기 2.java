import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> ans = new ArrayList<>();
        
        outer: for (int i = l; i <= r; i++) {
            String str = String.valueOf(i);
            
            for (char c : str.toCharArray()) {
                if (c != '0' && c != '5') {
                    continue outer; 
                }
            }

            ans.add(i); 
        }

        return ans.isEmpty() ? new int[]{-1} : ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
