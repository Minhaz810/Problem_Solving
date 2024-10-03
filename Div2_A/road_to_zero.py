t = int(input())
ans = []
for i in range(t):
    x,y = map(int,input().split())
    a,b = map(int,input().split())

    if a*(x+y) < (b*min(x,y)+a*(max(x,y)-min(x,y))):
        ans.append(a*(x+y))
    else:
        coins = b*min(x,y)+a*(max(x,y)-min(x,y))
        ans.append(coins)

for i in ans:
    print(i)