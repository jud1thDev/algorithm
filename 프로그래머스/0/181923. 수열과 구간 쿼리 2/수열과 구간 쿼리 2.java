class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] ans = new int[queries.length];
        int idx = 0; 
        
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            int k = query[2];
            
            int min = -1; 
            for (int i = s; i <= e; i++) {
                if (arr[i] > k) {
                    if (min == -1 || arr[i] < min) { 
                        min = arr[i];
                    }
                }
            }
            ans[idx++] = min;
        }
        return ans;
    }
}
