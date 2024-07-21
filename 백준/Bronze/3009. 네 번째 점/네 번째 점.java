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

        // Sol1)
        // int x1 = Integer.parseInt(st.nextToken());
        // int y1 = Integer.parseInt(st.nextToken());

        // st = new StringTokenizer(br.readLine());
        // int x2 = Integer.parseInt(st.nextToken());
        // int y2 = Integer.parseInt(st.nextToken());

        // st = new StringTokenizer(br.readLine());
        // int x3 = Integer.parseInt(st.nextToken());
        // int y3 = Integer.parseInt(st.nextToken());


        // Sol2) 반복되는 부분을 없앨 순 없을까?
        int[] x = new int[3];
        int[] y = new int[3];
        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken());
            y[i] = Integer.parseInt(st.nextToken());
        }

        int x4, y4;
        if (x[0] == x[1]) x4 = x[2];
        else if (x[1] == x[2]) x4 = x[0];
        else x4 = x[1];

        if (y[0] == y[1]) y4 = y[2];
        else if (y[1] == y[2]) y4 = y[0];
        else y4 = y[1];

        bw.write(x4 + " " + y4 + "\n");

        bw.flush();
        bw.close();
        br.close();
    }
}
