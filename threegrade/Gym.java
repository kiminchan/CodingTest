package threegrade;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Gym {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int Byte = N / 4;

        for (int i = 0; i < Byte; i++) {
            System.out.print("long ");
        }
        System.out.print("int");

    }
}
