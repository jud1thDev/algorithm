import java.util.*;

class Solution {
    private int addMinutes(int time, int minutes) {
        int hour = time / 100; 
        int minute = time % 100; 
        minute += minutes;
        if (minute >= 60) { // 60분 넘으면 시간 증가
            hour += 1;
            minute -= 60;
        }
        return hour * 100 + minute;
        }
    
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int count = 0; 
        
        for (int i = 0; i < schedules.length; i++){ // 직원수
            int hopeIn = schedules[i]; // 출근 희망 시각
            int successfulDays = 0;
            int currentday = startday;
                  
            for (int clockIn : timelogs[i]){
                int workday = currentday % 7;
                currentday++;
                
                if (workday == 6 || workday == 0) continue;
                
                int limitTime = addMinutes(hopeIn, 10);
                if (hopeIn >= clockIn || clockIn <= limitTime){
                    successfulDays++;
                }
            }
            
            if (successfulDays == 5) count++;
        }
        return count;
    }
}