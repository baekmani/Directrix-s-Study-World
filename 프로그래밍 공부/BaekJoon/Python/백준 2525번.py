import sys

hour, min = map(int, sys.stdin.readline().split())
cook = int(sys.stdin.readline())

min = min + cook

while min >= 60:
    hour += 1
    min -= 60

if hour >= 24:
    hour -= 24

print(hour, min)