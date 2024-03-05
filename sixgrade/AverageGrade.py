# 졸업하기 위해서는 전공 평점이 3.3이상이거나 졸업고사 통과
# 치훈이는 졸업고사를 응시하지 않았다

# 결국, 전공평점이 3.3이상이여야 졸업가능 

# 전공 평점 = 전공과목별의 합을 학점의 총합으로 나눈 값

# P/F 과목의 경우 등급이 P 또는 F로 표시되는데 등급이 
# P인 과목은 계산에서 제외 

# 입력 
# 20줄에 걸쳐 과목명, 학점, 등급 
import sys 

read = sys.stdin.readline

# 학점의 총합 
total_score = 0.0 

# 학점 x 과목평점
total = 0.0

# 전공 평점 
major_score = 0.0

# 과목평점 성적표
subject_grade = {'A+' : 4.5, 'A0': 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

for i in range(20):
    score_information = list(read().split())
    # P등급일 경우 패스 
    if score_information[2] == 'P':
        continue

    # 과목 평점 
    for i in range(len(subject_grade)):
        if score_information[2] in subject_grade:
            sum = 0 
            sum = subject_grade[score_information[2]] * float(score_information[1])
            total_score += float(score_information[1])
            total += sum

# 출력
# 전공평점 출력 
print(round(total/total_score, 6))

