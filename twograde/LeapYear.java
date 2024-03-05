package twograde;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class LeapYear {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int year = Integer.parseInt(br.readLine());
        // 연도가 주어졌을때, 윤년이면 1, 아니면 0

        // 윤년의 조건
        // 1. 4의 배수 이면서 100의 배수가 아닐 때
        // 2. 100의 배수이면서 400의 배수가 아닐 때

        if ((year % 4 == 0 && year % 100 != 0) || (year % 4 == 0 && year % 400 == 0)) {
            System.out.println("1");
        } else {
            System.out.println("0");
        }

    }
}
