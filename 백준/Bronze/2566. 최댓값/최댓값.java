import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[][] arr = new int[9][9];

        // 초기화
        int maxVal = 0; 
        int maxRow = 1;
        int maxCol = 1;

        for (int i = 0; i< 9; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++){
                arr [i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] > maxVal){
                    maxVal = arr [i][j];
                    maxRow = i + 1;
                    maxCol = j + 1;
                }
            }
        }
        bw.write(maxVal + "\n");
        bw.write(maxRow + " " + maxCol);
        br.close();
        bw.flush();
        bw.close();
    }
}