import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int[][] area = new int[100][100];
        int paperNum = scanner.nextInt();

        for (int i = 0; i < paperNum; i++){
            int x = scanner.nextInt();
            int y = scanner.nextInt();

            for (int dx = 0; dx < 10; dx++) {
                for (int dy = 0; dy < 10; dy++) {
                    area[x + dx][y + dy] = 1;
                }
            }
        }

        int coveredArea =  0;
        for(int i=0; i<100; i++){
            for(int j=0; j<100; j++){
                if (area[i][j] == 1) {
                    coveredArea++;
                }
            }
        }

        System.out.println(coveredArea);
        
    }
}