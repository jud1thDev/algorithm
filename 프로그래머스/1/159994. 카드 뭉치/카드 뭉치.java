import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        Queue<String> que1 = new LinkedList<>();
        Queue<String> que2 = new LinkedList<>();
        
        // 배열을 큐로 변환
        for (String card : cards1) que1.offer(card);
        for (String card : cards2) que2.offer(card);
        
        // goal의 단어 앞에서부터 순차적으로 확인
        for (String word : goal) {
            if (!que1.isEmpty() && que1.peek().equals(word)){
                que1.poll(); // 단어 사용
            } else if (!que2.isEmpty() && que2.peek().equals(word)){
                que2.poll(); // 단어 사용
            } else {
                return "No";
            }
        }
        return "Yes";
    }
}