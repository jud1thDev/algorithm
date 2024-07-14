import java.util.*;

public class Main  {
    static ArrayList<Integer> cards = new ArrayList<>();

    public static void main(String [] args){
    
        Scanner scanner = new Scanner(System.in);

        int[] num = new int[5];
        for (int i = 0; i < 5; i++) {
            int input = scanner.nextInt();
            // 유효성
            if(input % 10 == 0 && input < 100){num[i] = input;}
                else return;
        }

        Arrays.sort(num); // 오름차순 정렬
        System.out.println(Arrays.stream(num).sum()/5); // 평균값
        System.out.print(num[2]); //  중앙값
    }

}