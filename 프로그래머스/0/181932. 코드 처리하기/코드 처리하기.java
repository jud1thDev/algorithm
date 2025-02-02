class Solution {
    public String solution(String code) {
        StringBuilder ret = new StringBuilder();
        int mode = 0; 

        for (int idx = 0; idx < code.length(); idx++) { 
            char c = code.charAt(idx);

            if (mode == 0) {
                if (c == '1') {
                    mode = 1; 
                } else if (idx % 2 == 0) { 
                    ret.append(c);
                }
            } else { 
                if (c == '1') {
                    mode = 0; 
                } else if (idx % 2 == 1) { 
                    ret.append(c);
                }
            }
        }

        return ret.length() == 0 ? "EMPTY" : ret.toString();
    }
}
