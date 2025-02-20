import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int len = num_list.length;
        int n = num_list[len - 1];
        int m = num_list[len - 2];
        int new_element = (n > m) ? (n - m) : 2*n;
        int[] ans = Arrays.copyOf(num_list, len + 1);
        ans[len] = new_element;
        return ans;
    }
}