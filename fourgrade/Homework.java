package fourgrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Homework {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[30];

        for (int i = 1; i <= 30; i++) {
            arr[i - 1] = 0;
        }

        for (int i = 0; i < 28; i++) {
            int number = Integer.parseInt(br.readLine());
            arr[number - 1] = 1;
        }

        for (int i = 1; i <= 30; i++) {
            if (arr[i - 1] != 1) {
                System.out.println(i);
            }
        }
    }
}
