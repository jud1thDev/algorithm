import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] result = new int[photo.length];
        
        Map<String, Integer> yearningMap = new HashMap<>();
        for (int i = 0; i < name.length; i++){
            yearningMap.put(name[i], yearning[i]);
        }
        
        for (int i = 0; i < photo.length; i++) {
            int sum = 0;
            for (String person : photo[i]) {
                sum += yearningMap.getOrDefault(person, 0);
            }
            result[i] = sum;
        }
        return result;
    }
}