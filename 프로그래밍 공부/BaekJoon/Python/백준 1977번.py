start = int(input())
end = int(input())

num = []

for i in range(int(start**0.5), int(end**0.5)+1):
    if start <= i*i <= end:
        num.append(i*i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))