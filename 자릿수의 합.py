def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x //= 0 #x = x//10
    return sum

n = int(input())
k = list(map(int, input().split()))
res = 0
max = -2147000000
for x in k:
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x
print(res)
