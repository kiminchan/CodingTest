package fourgrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BallChange {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st, st1;
        String str, str1;

        str = br.readLine();

        st = new StringTokenizer(str, " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] basket = new int[N];

        for (int i = 1; i <= N; i++) {
            basket[i - 1] = i;
        }

        for (int i = 0; i < M; i++) {
            str1 = br.readLine();
            st1 = new StringTokenizer(str1, " ");
            int a = Integer.parseInt(st1.nextToken());
            int b = Integer.parseInt(st1.nextToken());
            int number = 0;

            number = basket[a - 1];
            basket[a - 1] = basket[b - 1];
            basket[b - 1] = number;

        }

        for (int i = 0; i < N; i++) {
            System.out.print(basket[i] + " ");
        }

    }
}
