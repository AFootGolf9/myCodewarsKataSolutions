

import random


def interpret(code):
    output = ""
    stack = []
    x=0
    y=0
    difY = 1
    difX = 0
    stringMode = False


    code = code.split('\n')

    while(code[x][y] != '@'):
        if stringMode:
            if code[x][y] == '\"':
                stringMode = False
            else:
                stack.append(ord(code[x][y]))
        else:
            match code[x][y]:
                case ' ':
                    nothing = 0
                case '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                case '-':
                    a = stack.pop()
                    stack.append(int(stack.pop()) - int(a))
                case '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                case '/':
                    a = stack.pop()
                    stack.append(int(stack.pop()) / int(a))
                case '%':
                    a = stack.pop()
                    b = stack.pop()
                    if a == '0':
                        stack.append(0)
                    else:
                        stack.append(int(b)%int(a))
                case '!':
                    if stack.pop == '0':
                        stack.append('1')
                    else:
                        stack.append('0')
                case '`':
                    if stack.pop() < stack.pop():
                        stack.append('1')
                    else:
                        stack.append('0')
                case '>':
                    difY = 1
                    difX = 0
                case '<':
                    difY = -1
                    difX = 0
                case '^':
                    difY = 0
                    difX = -1
                case 'v':
                    difY = 0
                    difX = 1
                case '?':
                    match random.randrange(0,4):
                        case 0:
                            difY = 1
                            difX = 0
                        case 1:
                            difY = -1
                            difX = 0
                        case 2:
                            difY = 0
                            difX = -1
                        case 3:
                            difY = 0
                            difX = 1
                case '_':
                    if stack.pop() == '0':
                        difY = 1
                        difX = 0
                    else:
                        difY = -1
                        difX = 0
                case '|':
                    if stack.pop() == '0':
                        difX = 1
                        difY = 0
                    else:
                        difX = -1
                        difY = 0
                case '\"':
                    stringMode = True
                case ':':
                    if len(stack) == 0:
                        stack.append('0')
                    else:
                        a = stack.pop()
                        stack.append(a)
                        stack.append(a)
                case '\\':
                    match len(stack):
                        case 1:
                            stack.append('0')
                        case 0:
                            stack.append('0')
                            stack.append('0')
                        case _:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(a)
                            stack.append(b)
                case '$':
                    stack.pop()
                case '.':
                    output += stack.pop()
                case ',':
                    output += chr(int(stack.pop()))
                case '#':
                    x += difX
                    y += difY
                case 'p':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    code[b][a] = stack.pop()
                case 'g':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(code[a][b])
                case _:
                    stack.append(code[x][y])
        
        x += difX
        y += difY

    # TODO: Interpret the code!
    return output

print(interpret("01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"))