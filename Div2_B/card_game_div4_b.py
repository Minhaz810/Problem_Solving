t = int(input())
ans =[]
 
for i in range(t):
    a,b,c,d = map(int,input().split())
 
    if a>c and a>d and b>=c and b>=d:
        ans.append(4)
    elif a>=c and a>=d and b>c and b>d:
        ans.append(4)
    elif a<=c and a<=d and b<=c and b<=d:
        ans.append(0)
    else:
        ans.append(2)
 
for i in ans:
    print(i)