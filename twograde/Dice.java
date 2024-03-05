package twograde;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Dice {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        // 1~6까지의 눈을 가진 주사위 3개를 던져 규칙에 따라 상금

        // 입력 : 주사위 눈 3개
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        // 1. 같은 눈 3개 : 10,000원+(같은 눈)x 1,000원
        // 2. 같은 눈 2개 : 1,000원 +(같은 눈)x 100원
        // 3. 모두 다른 눈 : (그 중 가장 큰 눈)x 100원
        int prize = 0;
        int high = 0;

        if (a == b && b == c && a == c) {
            prize += 10000 + (a * 1000);
        } else if (a == b || b == c || a == c) {
            if (a == b) {
                prize += 1000 + (a * 100);
            } else if (b == c) {
                prize += 1000 + (b * 100);
            } else {
                prize += 1000 + (a * 100);
            }
        } else {
            if (high < a) {
                high = a;
            }
            if (high < b) {
                high = b;
            }
            if (high < c) {
                high = c;
            }
            prize += high * 100;
        }

        System.out.println(prize);
    }
}
