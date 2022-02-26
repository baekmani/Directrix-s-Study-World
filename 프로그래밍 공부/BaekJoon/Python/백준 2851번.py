from collections import deque

mush = deque()
for i in range(10):
    mush.append(int(input()))

sum = []
real = []
score = 0
stop = 0
for i in range(10):
    a = mush.popleft()
    score += a
    if stop == 1: break
    if score >= 100:
        stop = 1
    sum.append(score)

try:
    if abs(100-sum[-1]) > abs(100-sum[-2]):
        print(sum[-2])
    else:
        print(sum[-1]) 
except:
    print(sum[0])