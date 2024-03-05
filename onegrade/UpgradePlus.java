package onegrade;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class UpgradePlus {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // String[] strs = br.readLine().split(" ");

        // long a = Long.valueOf(strs[0]);
        // long b = Long.valueOf(strs[1]);
        // long c = Long.valueOf(strs[2]);

        long a = Long.valueOf(st.nextToken());
        long b = Long.valueOf(st.nextToken());
        long c = Long.valueOf(st.nextToken());

        System.out.println(a + b + c);
    }
}
