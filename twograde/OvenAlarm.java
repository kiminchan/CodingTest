package twograde;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class OvenAlarm {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 훈제오리구이를 시작하는 시각과 오븐구이를 하는데 필요한 시간이 분단위 주어짐
        // 오븐구이가 끝나는 시각을 계산

        // 입력
        // 첫째줄 : 현재 시각 H M
        int H = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        // 둘째줄 : 요리하는데 필요한 시간 ct(cookingtime)
        int cookingtime = Integer.parseInt(br.readLine());
        int min = (H * 60) + M + cookingtime;

        // 출력
        // 첫째줄 : 종료되는 H M
        int endH = (min / 60) % 24;
        int endM = min % 60;
        System.out.println(endH + " " + endM);

    }
}
