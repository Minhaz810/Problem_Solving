t = int(input())
ans = []

for i in range(t):
    p1,p2,p3 = map(int,input().split())

    a1,a2,a3 = 0, 0, 0
    count = 0
    if (p1+p2+p3)%2 != 0:
        ans.append(-1)
    else:
        while a2<p2:
            a3+=1
            a2+=1
            count +=1
        
        if a3 != p3:
            while a1<p1:
                a3+=1
                a1+=1
            count+=1
        ans.append(count)
for i in ans:
    print(i)