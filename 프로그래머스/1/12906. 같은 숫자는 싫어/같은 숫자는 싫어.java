import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        StringBuilder sb = new StringBuilder();
        
        sb.append(arr[0]);
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i - 1]) {
                sb.append(arr[i]);
            }
        }
        
        int[] result = new int[sb.length()];
        for (int i=0; i<sb.length(); i++){
            result[i] = sb.charAt(i) - '0';
        }
        
        return result;
    }
}