class Solution {
    public int solution(int a, int b, int c) {
        int ans = 0;

        if (a != b && b != c && c != a) {
            ans = a + b + c;
        } else if (a == b && b == c) {
            ans = (a + b + c) * ((a * a) + (b * b) + (c * c)) * ((a * a * a) + (b * b * b) + (c * c * c));
        } else {
            ans = (a + b + c) * ((a * a) + (b * b) + (c * c));
        }

        return ans;
    }
}
