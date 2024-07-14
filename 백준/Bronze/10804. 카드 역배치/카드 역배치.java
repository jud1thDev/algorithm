import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer> cards = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 카드 20장
        for (int i = 1; i <= 20; i++) {
            cards.add(i);
        }

        // 총 10개의 구간 입력, 인덱스와 맞추기 위해 -1
        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            reverse(a, b);
        }

        for (int i : cards) {
            bw.write(i + " ");
        }
        bw.newLine();
        
        bw.flush();
        bw.close();
        br.close();
    }

    static void reverse(int start, int end) {
        ArrayList<Integer> temp = new ArrayList<>();
        for (int i = start; i <= end; i++) {
            temp.add(cards.get(start));
            cards.remove(start);
        }
        for (int i = 0; i < temp.size(); i++) {
            cards.add(start + i, temp.get(temp.size() - 1 - i));
        }
    }
}
