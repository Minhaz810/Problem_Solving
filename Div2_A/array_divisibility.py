n = int(input())
ans = []
for i in range(n):
    n = int(input())
    li =[]
    element = 1
    for i in range(1,n+1):
        li.append(i)
    
    ans.append(li)


for arr in ans:
    for el in arr:
        print(el,end=" ")
    print()


