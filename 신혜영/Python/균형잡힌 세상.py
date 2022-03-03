import sys

input = sys.stdin.readline
flag = True
while True:
    str = input()
    stack = []

    if str == '.':
        break

    for i in str:
        if i == '[' or i == '(':
            stack.append(i)

        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
    
    if flag:
        print('yes')
    else:
        print('no')
