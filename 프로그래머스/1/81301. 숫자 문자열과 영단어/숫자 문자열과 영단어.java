class Solution {
    public int solution(String s) {
        StringBuilder sb = new StringBuilder();
        StringBuilder temp = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            if (Character.isDigit(ch)) {
                sb.append(ch);
            } else {
                temp.append(ch);
                String word = temp.toString();
                int digit = convertWordToDigit(word);
                if (digit != -1) {
                    sb.append(digit);
                    temp.setLength(0); // 초기화
                }
            }
        }
        return Integer.parseInt(sb.toString());
    }

    private int convertWordToDigit(String word) {
        switch (word) {
            case "zero": return 0;
            case "one": return 1;
            case "two": return 2;
            case "three": return 3;
            case "four": return 4;
            case "five": return 5;
            case "six": return 6;
            case "seven": return 7;
            case "eight": return 8;
            case "nine": return 9;
            default: return -1;
        }
    }
}
