import sys

read = sys.stdin.readline

a, b = read().split()


# 문자열 거꾸로 출력하는 방법 
reverse_a = a[::-1]
reverse_b = b[::-1]
if reverse_a > reverse_b:
    print(int(reverse_a))
else:
    print(int(reverse_b))


# reversed(), join() 사용 
# string = "hello world"
# reversed_string = ''.join(reversed(string))

# print(reversed_string)


