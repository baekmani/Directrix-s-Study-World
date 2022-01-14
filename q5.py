# 선택된 집들 중에서 가장 가운데에 있는 집을 선택

import sys
input = sys.stdin.readline

cnt = int(input())
house = list(map(int, input().split()))
house.sort()
print(house[int((cnt-1)/2)])
