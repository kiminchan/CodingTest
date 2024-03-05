package fourgrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SmallNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String str, str1;

        // 입력
        str1 = br.readLine();
        st = new StringTokenizer(str1, " ");
        // N : 수열 A를 이루는 정수 개수
        int N = Integer.parseInt(st.nextToken());

        // X : 기준이 되는 정수
        int X = Integer.parseInt(st.nextToken());

        // 수열 A
        int[] arr = new int[N];

        str = br.readLine();
        st = new StringTokenizer(str, " ");
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 출력
        // X보다 작은 수를 입력 받은 순서대로 공백으로 구분해 출력
        // X보다 작은 수는 적어도 하나 존재
        int[] arr1 = new int[N];
        int count = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i] < X) {
                arr1[count] = arr[i];
                count += 1;
            }
        }

        for (int i = 0; i < count; i++) {
            System.out.print(arr1[i] + " ");
        }

    }
}
