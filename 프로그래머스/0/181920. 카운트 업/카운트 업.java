class Solution {
    public int[] solution(int start_num, int end_num) {
        int size = end_num - start_num + 1;
        int[] arr = new int[size];
        for (int i = 0; i < size; i++){
            arr[i] = start_num + i;
        }
        return arr;
    }
}