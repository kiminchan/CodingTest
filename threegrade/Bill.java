package threegrade;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Bill {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        // X : 영수증에 적힌 총 금액
        int X = Integer.parseInt(br.readLine());
        // N : 구매한 물건의 종류의 수
        int N = Integer.parseInt(br.readLine());

        // 물건 계산 가격
        int total = 0;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // a : 물건의 가격
            int a = Integer.parseInt(st.nextToken());

            // b : 물건의 개수
            int b = Integer.parseInt(st.nextToken());

            total += (a * b);
        }

        // 출력
        // 구매한 가격의 개수로 계산한 총액 == 영수증 총액 Yes
        // 아니면 No
        if (total == X) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }

}
