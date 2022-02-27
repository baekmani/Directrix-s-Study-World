import sys
loop = int(sys.stdin.readline())
rec = []
num = 0
for i in range(loop):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        num -= rec.pop()
    else:
        num += tmp
        rec.append(tmp)
    print(num, rec)
print(num)