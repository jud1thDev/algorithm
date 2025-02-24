import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> ans = new ArrayList<>();
        
        while (n != 1) {
            ans.add(n);
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
        }
        
        ans.add(1); 

        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
