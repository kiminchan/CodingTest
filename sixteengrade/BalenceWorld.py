# 모든 외쪽 소괄호는 오른쪽 소괄호와만 짝을 이루어야 한다
# 모든 왼쪽 대괄호는 오른쪽 대괄호와만 짝을 이루어야 한다
# 모든 오른쪽 괄호들은 자신과 짝을 이룰수있는 왼쪽 괄호가 존재 
# 모든 괄호들의 짝은 1:1 매칭만 가능하다 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다
# 짝을 이루는 두 괄호가 있을때, 그 사이에 있는 문자열도 균형이 잡혀야 한다 
import sys

while True:
    str = input()
    
    stack = []
    is_Balence = True
    if str ==".":
        break
    '''
    for i in str:
        if i == '[' or i =='(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
            
        elif i ==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    '''
    for i in str:
        if i == '[' or i =='(':
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] != '(':
                is_Balence = False
                break
            stack.pop()
        elif i == "]":
            if not stack or stack[-1] != '[':
                is_Balence = False
                break
            stack.pop()
    
    if is_Balence and not stack:
        print("yes")
    else:
        print("no")
