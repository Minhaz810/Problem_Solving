t = int(input())
ans = []

for i in range(t):
    n = int(input())
    x,y = map(int,input().split())
    
    if x<y:
        if n%x == 0:
            ans.append(n//x)
        else:
            ans.append(n//x+1)
    else:
        if n%y == 0:
            ans.append(n//y)
        else:
            ans.append(n//y+1)

for i in ans:
    print(i)
        