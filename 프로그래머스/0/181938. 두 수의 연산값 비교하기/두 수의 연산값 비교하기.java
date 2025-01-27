class Solution {
    public int solution(int a, int b) {
        int sum1 = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int sum2 = 2*a*b;
        return Math.max(sum1, sum2);
    }
}