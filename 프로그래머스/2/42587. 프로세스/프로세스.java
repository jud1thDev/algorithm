import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        
        List<Integer> priorityList = new ArrayList<>();
        for (int p : priorities){
            priorityList.add(p);
        }
        priorityList.sort(Collections.reverseOrder());
        
        int currentPriority = 0;
        boolean found = false;
        
        while (found == false){
            for (int i = 0; i < priorities.length; i++){
                if (priorities[i] == priorityList.get(currentPriority)){
                    if (i == location){
                        found = true;
                        break;
                    }
                    answer ++;
                    currentPriority++;
                }
            }
        }
        return answer;
    }
}