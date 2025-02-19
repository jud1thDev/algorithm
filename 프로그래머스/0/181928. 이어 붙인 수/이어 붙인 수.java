class Solution {
    public int solution(int[] num_list) {
        StringBuilder oddsum = new StringBuilder();
        StringBuilder evensum = new StringBuilder();
        for (int num : num_list) {
            if (num % 2 == 0) {
                oddsum.append(num);
            } else evensum.append(num);
        }
        return Integer.parseInt(oddsum.toString()) + Integer.parseInt(evensum.toString());
    }
}