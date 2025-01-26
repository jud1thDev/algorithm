import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        Map<String, Map<String, Integer>> giftMap = new HashMap<>();
        Map<String, Integer> scoreMap = new HashMap<>();

        // 선물 기록 저장
        for (String gift : gifts) {
            String[] tmp = gift.split(" ");
            String giver = tmp[0];
            String receiver = tmp[1];

            scoreMap.put(giver, scoreMap.getOrDefault(giver, 0) + 1);
            scoreMap.put(receiver, scoreMap.getOrDefault(receiver, 0) - 1);

            Map<String, Integer> map = giftMap.getOrDefault(giver, new HashMap<>());
            map.put(receiver, map.getOrDefault(receiver, 0) + 1);
            giftMap.put(giver, map);
        }

        Map<String, Integer> receiveCntMap = new HashMap<>();
        int answer = 0;

        int friendsLen = friends.length;
        for (int i = 0; i < friendsLen - 1; i++) {
            String giver = friends[i];
            Map<String, Integer> giverMap = giftMap.getOrDefault(giver, new HashMap<>());

            for (int j = i + 1; j < friendsLen; j++) {
                String receiver = friends[j];
                Map<String, Integer> receiverMap = giftMap.getOrDefault(receiver, new HashMap<>());

                int giveCnt = giverMap.getOrDefault(receiver, 0) - receiverMap.getOrDefault(giver, 0);

                if (giveCnt == 0) {
                    giveCnt = scoreMap.getOrDefault(giver, 0) - scoreMap.getOrDefault(receiver, 0);
                }

                if (giveCnt > 0) {
                    int receiveCnt = receiveCntMap.getOrDefault(giver, 0) + 1;
                    receiveCntMap.put(giver, receiveCnt);
                    answer = Math.max(answer, receiveCnt);
                } else if (giveCnt < 0) {
                    int receiveCnt = receiveCntMap.getOrDefault(receiver, 0) + 1;
                    receiveCntMap.put(receiver, receiveCnt);
                    answer = Math.max(answer, receiveCnt);
                }

                // 관계를 한 번 계산한 후, 중복 방지를 위해 데이터 수정
                giverMap.remove(receiver);
                receiverMap.remove(giver);
            }
        }
        return answer;
    }
}
