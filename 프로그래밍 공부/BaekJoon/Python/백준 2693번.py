a = int(input())

for i in range(a):
    numList = list(map(int, input().split()))
    numList.sort(reverse=True)
    print(numList)
    print(numList[2])