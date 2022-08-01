# n, m = map(int, input().split())
# number = list(map(int, input().split()))
# cnt = 0
# for i in range(n):
#     if number[i] + number[i-1] == m:
#         cnt += 1
#     elif number[i] == m:
#         cnt += 1
#     elif number[i-2] + number[i-1] < m and number[i] + number[i-1] + number[i-2] == 3:
#         cnt += 1
# print(cnt-1)

n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)