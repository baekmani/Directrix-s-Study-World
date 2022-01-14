def solution(k, a, b):
    answer = []
    for i in range(k):
        maxb = b.pop(b.index(max(b)))
        a[a.index(min(a))] = maxb
        answer.append(sum(a))
    print(answer)
    return max(answer)

k = 3

a = [1,2,5,4,3, 6]
b = [5,5,6,6,5, 1]
answer = solution(k, a, b)
print(answer)
