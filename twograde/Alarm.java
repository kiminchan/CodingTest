package twograde;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Alarm {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int H = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 45분 알람 일찍 설정 하기

        // 하루의 시작 0:00 , 하루의 끝은 23:59
        // 시간 나타낼때 불필요한 0은 사용하지 않는다.

        // 1. M이 45분이상일 경우

        // 2. M이 45보다 작을 경우
        // H를 1 감소시키고 M에다가 60을 더해준 뒤 계산

        // 3. H가 0일때, M이 45보다 작을 경우
        // H를 23으로 변경해주고 60- (45-원래 M)

        if (H != 0) {
            if (M >= 45) {
                System.out.println(H + " " + (M - 45));
            } else {
                System.out.println((H - 1) + " " + (60 - (45 - M)));
            }
        } else {
            if (M >= 45) {
                System.out.println(H + " " + (M - 45));
            } else {
                System.out.println(23 + " " + (60 - (45 - M)));
            }
        }

    }
}
