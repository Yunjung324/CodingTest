#1
n = int(input())
for i in range(n):
    str = input()
    str = str.upper()
    if str == str[::-1]:
        print("#%d YES" %i)
    else:
        print("#%d NO" %i)

#2
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res*10+int(x)
    print(res)
    cnt = 0
    for i in range(1, res+1):
        if res%i == 0:
            cnt+=1
    print(cnt)
