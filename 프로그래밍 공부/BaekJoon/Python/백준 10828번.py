# 시간초과로 sys 지키고, pypy3로 제출했음

import sys
a = int(sys.stdin.readline())
numList = []
for i in range(a):
    order_list = list(sys.stdin.readline().split())
    if len(order_list) == 2:
        order = order_list[0]
        num = order_list[1]
    else :
        order = order_list[0]
    try:
        if order == 'push':
            numList.append(num)
        elif order == 'pop':
            print(numList.pop())
        elif order == 'empty':
            if len(numList) == 0:
                print(1)
            else:
                print(0)
        elif order == 'size':
            print(len(numList))
        elif order == 'top':
            print(numList[-1])
    except :
        print(-1)