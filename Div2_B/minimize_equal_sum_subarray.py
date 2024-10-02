t = int(input())
ans = []

for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))

    f = li.pop(0)
    li.append(f)
    ans.append(li)

for i in ans:
    for j in i:
        print(j,end=" ")
    print()
