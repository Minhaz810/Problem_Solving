t = int(input())
ans = []

for i in range(t):
    n,m,k = map(int,input().split())
    li = []
    i = n

    for i in range(n,m,-1):
        li.append(i)
    for i in range(1,m+1):
        li.append(i)


    ans.append(li)

for i in ans:
    for j in i:
        print(j,end=" ")
    print()

