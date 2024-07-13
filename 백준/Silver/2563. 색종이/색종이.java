import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int[][] area = new int[100][100];
    int paperNum = Integer.parseInt(br.readLine());

    for (int i = 0; i < paperNum; i++){
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        for (int dx = 0; dx < 10; dx++){
            for (int dy = 0; dy < 10; dy++){
                area[x + dx][y + dy] = 1;
            }
        }
    }
    int coveredArea = 0;
    for (int i = 0; i < 100; i++){
        for (int j = 0; j < 100; j++){
            if (area[i][j] == 1) coveredArea++;
        }
    }
    bw.write(String.valueOf(coveredArea));
    br.close();
    bw.flush();
    bw.close();
    }
}