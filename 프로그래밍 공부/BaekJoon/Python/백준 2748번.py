a = int(input())
on = 0
two = 1
sum = 0
for i in range(a):
    on = two
    two = sum
    sum = on + two
print(sum)