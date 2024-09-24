t = int(input())
ans = []

for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))

    if len(li) == 2:
        ans.append(li[1]-li[0])
    else:
        temp = []
        for i in range(len(li)-2):
            temp.append(li[i])
        temp = sorted(temp,reverse= True)
        for i in temp:
            li[len(li)-2] -=i
        ans.append(li[len(li)-1]-li[len(li)-2])

for i in ans:
    print(i)
    
    


