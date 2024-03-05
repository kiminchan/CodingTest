package fourgrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class MinMax {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String str;

        // 입력
        // N : 정수의 개수
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        // N개의 정수를 공백으로 구분
        str = br.readLine();
        st = new StringTokenizer(str, " ");
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int min = arr[0];
        int max = arr[0];
        for (int i = 1; i < N; i++) {
            if (arr[i] < min) {
                min = arr[i];
            } else if (arr[i] > max) {
                max = arr[i];
            }
        }
        // 출력
        // N개의 최솟값과 최댓값을 공백으로 구분해 출력
        System.out.println(min + " " + max);

    }
}
