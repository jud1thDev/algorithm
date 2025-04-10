class Solution {
    public String solution(String s) {
        int l = s.length();
        int ans = l/2;
        return (l % 2 != 0) ? s.substring(ans, ans+1) : s.substring(ans-1, ans+1);
    }
}