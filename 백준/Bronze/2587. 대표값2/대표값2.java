import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] num = new int[5];
        for (int i = 0; i < 5; i++) {
            int input = Integer.parseInt(br.readLine());
            // 유효성 검사
            if (input % 10 == 0 && input < 100) {
                num[i] = input;
            } else {
                return;
            }
        }

        Arrays.sort(num); // 오름차순 정렬
        int average = Arrays.stream(num).sum() / 5; // 평균값
        int median = num[2]; // 중앙값

        bw.write(String.valueOf(average));
        bw.newLine();
        bw.write(String.valueOf(median));
        bw.newLine();

        bw.flush();
        bw.close();
        br.close();
    }
}
