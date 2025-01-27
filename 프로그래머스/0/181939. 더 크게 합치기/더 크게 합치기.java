class Solution {
    public int solution(int a, int b) {
        StringBuilder sb = new StringBuilder();
        String sum1 = String.valueOf(a) + String.valueOf(b);
        String sum2 = String.valueOf(b) + String.valueOf(a);
        int num1 = Integer.parseInt(sum1);
        int num2 = Integer.parseInt(sum2);
        return Math.max(num1, num2);
    }
}