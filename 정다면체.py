n, m = map(int, input().split())
cnt = 0
list = []
for i in range(1,n+1):
    for j in range(1, m+1):
        list.append(i+j)
        print(list)
