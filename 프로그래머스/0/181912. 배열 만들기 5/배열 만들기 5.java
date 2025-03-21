import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < intStrs.length; i++){
            String cut = intStrs[i].substring(s, s + l);
            int num = Integer.parseInt(cut); 
            if (num > k){
                ans.add(num);
            }
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}