class Solution {
    public String solution(String s, int n) {
        StringBuilder result = new StringBuilder();
        char[] arr = s.toCharArray();
        for (char c : arr){
            if (Character.isUpperCase(c)) {
                char ch = (char) ((c -'A' + n) % 26 + 'A');
                result.append(ch);
            } else if (Character.isLowerCase(c)) {
                char ch = (char) ((c -'a' + n) % 26 + 'a');
                result.append(ch);
            } else {
                result.append(c); // 공백은 아무리 밀어도 공백
            }
        }
        return result.toString();
    }
}