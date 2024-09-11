n = int(input())

res = []
for i in range(n):
    t = int(input())
    li = []
    for i in range(t):
        coords = list(map(int,input().split()))
        li.append(coords)
    
    count_y_0 = 0
    count_y_1 = 0
    for i in li:
        if i[1] == 0:
            count_y_0+=1
        else:
            count_y_1+=1
    
    if count_y_0 == t or count_y_1 == t:
        res.append(0)


print(res)