class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isOdd = false;
        
        for (char c: s.toCharArray()){
            if (c == ' '){
                sb.append(c);
                isOdd = false; // 단어 기준 짝/홀이므로
            } else {
                if (isOdd) {
                    sb.append(Character.toLowerCase(c));
                } else {
                    sb.append(Character.toUpperCase(c));
                }
                isOdd = !isOdd; // flag 전환
            }
        }
             return sb.toString();
    }
}