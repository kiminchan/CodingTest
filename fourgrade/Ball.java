package fourgrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Ball {
    public static void main(String[] args) throws IOException {
        // 문제 설명
        // 도현이는 바구니를 총 N개 가지고 있음
        // 각각의 바구니에는 1번 ~ N번까지 번호가 있음
        // 또 1번 ~ N번까지 번호가 적혀있는 공을 매우 많이 가지고 있음
        // 가장 처음 바구니에는 공이 없음
        // 바구니에는 공 1개만 넣을 수 있음

        // 도현이는 앞으로 M번 공을 넣을려고 한다
        // 한 번 공을 넣을 때 :
        // 공을 넣을 바구니 범위를 정함
        // 정한 바구니에 모두 같은 번호가 적혀 있는 공을 넣는다.
        // 만약 바구니에 공이 이미 있는 경우는 들어있는 공을 빼고,
        // 새로 공을 넣는다.
        // 공을 넣을 바구니는 연속되어 있어야 한다.

        // 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에
        // 어떤 공이 들어 있는지 구하는 프로그램

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st, st1;
        String str, str1;

        // 입력

        str = br.readLine();

        st = new StringTokenizer(str, " ");
        // N : 도현이가 가지고 있는 바구니 개수
        int N = Integer.parseInt(st.nextToken());

        int[] basketArr = new int[N];

        for (int i = 0; i < N; i++) {
            basketArr[i] = 0;
        }

        // M : 도현이가 공을 넣는 횟수
        int M = Integer.parseInt(st.nextToken());

        // i j k : i번 바구니 ~ j번 바구니에 k번 번호가 적혀져 있는 공을 넣음
        // ex) 2 5 6은 2번 바구니 ~ 5번 바구니까지에 6번공을 넣음
        for (int i = 0; i < M; i++) {
            str1 = br.readLine();
            st1 = new StringTokenizer(str1, " ");
            int start = Integer.parseInt(st1.nextToken());
            int end = Integer.parseInt(st1.nextToken());
            int number = Integer.parseInt(st1.nextToken());

            for (int j = start - 1; j < end; j++) {
                basketArr[j] = number;
            }

        }

        // 출력
        // 1번 바구니부터 N번 바구니에 들어 있는 공의 번호를 공백으로 구분해 출력
        for (int i = 0; i < N; i++) {
            System.out.print(basketArr[i] + " ");

        }
    }

}
