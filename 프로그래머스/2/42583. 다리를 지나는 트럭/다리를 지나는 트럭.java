import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        Queue<Integer> waiting = new LinkedList<>();
        
        for (int truck : truck_weights){
            waiting.offer(truck);
        }
        
        int time = 0;
        int bridgeWeight = 0;
        
        for (int i = 0; i < bridge_length; i++){
            bridge.offer(0);
        }
        
        while (!bridge.isEmpty()){
            time++;
            
            bridgeWeight -= bridge.poll();
            
            if (!waiting.isEmpty()){
                if (bridgeWeight + waiting.peek() <= weight){
                    int nextTruck = waiting.poll();
                    bridge.offer(nextTruck);
                    bridgeWeight += nextTruck;
                } else bridge.offer(0);
            }
        }
        return time; 
    }
}