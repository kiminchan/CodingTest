package onegrade;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Year {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int byear = Integer.parseInt(br.readLine());

        System.out.println(byear - 543);
    }

}
