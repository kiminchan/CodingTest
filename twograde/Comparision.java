package twograde;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Comparision {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] strs = br.readLine().split(" ");

        int a = Integer.parseInt(strs[0]);
        int b = Integer.parseInt(strs[1]);

        if (a < b) {
            System.out.println("<");
        } else if (a > b) {
            System.out.println(">");
        } else {
            System.out.println("==");
        }
    }
}
