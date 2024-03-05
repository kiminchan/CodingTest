package fourgrade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Max {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];

        for (int i = 0; i < 9; i++) {
            int number = Integer.parseInt(br.readLine());
            arr[i] = number;
        }

        int max = 0;
        int sequence = 0;
        if (arr[0] < arr[1]) {
            max = arr[1];
            sequence = 2;
        } else if (arr[0] > arr[1]) {
            max = arr[0];
            sequence = 1;
        }
        for (int i = 2; i < 9; i++) {
            if (max < arr[i]) {
                max = arr[i];
                sequence = i + 1;
            }
        }
        System.out.println(max);
        System.out.println(sequence);
    }
}
