import sys

#def check(ps):


loop = int(sys.stdin.readline())
for i in range(loop):
    ps = list(sys.stdin.readline().strip())
    check = 0
    for j in ps:
        if j == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            print('NO')
            break
    else:
        if check != 0:
            print('NO')
        else:
            print('YES')