import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int count = 0;
        int result = 0;

        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {
                count++;
            }
            if (count == K) {
                result = i;
                break;
            }
        }

        // K번째 약수가 존재하지 않는 경우 0 출력
        if (count < K) {
            bw.write("0\n");
        } else {
            bw.write(result + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
