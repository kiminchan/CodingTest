package threegrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class StarUpgrade {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 1; i < T + 1; i++) {
            for (int j = T - i; j > 0; j--) {
                System.out.print(" ");
            }
            for (int k = 0; k < i; k++) {
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}
