package threegrade;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Sum {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int total = 0;
        for (int i = 1; i <= num; i++) {
            total += i;
        }
        System.out.println(total);
    }
}
