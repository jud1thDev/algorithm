import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] ans = new int[prices.length];
        Stack<Integer> protecting = new Stack<>();
        
        for(int i = 0; i < prices.length; i++){
            int current = prices[i];
            // 가격 떨어지는 경우 처리
            while(!protecting.isEmpty() && current < prices[protecting.peek()]){
                int top = protecting.pop();
                ans[top] = i - top;
            }
            protecting.push(i);
        }
        
        // 가격이 한 번도 안 떨어진 경우
        while (!protecting.isEmpty()){
            int top = protecting.pop();
            ans[top] = prices.length - top - 1;
        }
        return ans;
    }
}