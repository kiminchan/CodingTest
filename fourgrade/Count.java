package fourgrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Count {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String str;
        int count = 0;

        // 입력
        // N : 정수의 개수
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        str = br.readLine();
        st = new StringTokenizer(str, " ");
        // 정수가 공백으로 구분
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // v : 찾으려고 하는 정수
        int v = Integer.parseInt(br.readLine());

        // 출력
        // N 개의 정수 중에 v 가 몇 개 인지 출력
        for (int i = 0; i < N; i++) {
            if (arr[i] == v) {
                count += 1;
            }
        }
        System.out.println(count);

    }
}
