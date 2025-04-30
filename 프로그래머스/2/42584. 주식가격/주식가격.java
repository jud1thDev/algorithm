import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] ans = new int[prices.length];
        Stack<Integer> protecting = new Stack<>(); // 가격 방어중인 애들 idx
        
        for (int i = 0; i < prices.length; i++){
            while (!protecting.isEmpty() && prices[i] < prices[protecting.peek()]){ // 가격 떨어짐
                int top = protecting.pop();
                ans[top] = i - top;
            }
            protecting.push(i);
        }
        
        // 끝까지 가격이 안 떨어진 애들 처리
        while (!protecting.isEmpty()){
            int top = protecting.pop();
            ans[top] = prices.length - top - 1;
        }
        
        return ans;
    }
}