t= int(input())
ans = []

for i in range(t):
    b,c = map(int,input().split())
    a =list(map(int,input().split()))[:b]
    n =list(map(int,input().split()))[:c]

    li = []
    for i in n:
        if a[0]>i:
            li.append(i)
        else:
            li.append(a[0]-1)
    ans.append(li)


for i in ans:
    for j in i:
        print(j,end=" ")
    print()

    