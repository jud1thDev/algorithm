class Solution {
    public String solution(int[] numLog) {
        StringBuilder ans = new StringBuilder();
        int prev = numLog[0];
        for(int i=1; i<numLog.length; i++){
            int d = numLog[i] - prev;
            switch(d){
            case 1: ans.append("w"); break;
            case -1: ans.append("s"); break;
            case 10: ans.append("d"); break;
            case -10: ans.append("a"); break;
            }
            prev = numLog[i];
        }
        return ans.toString();
    }
}