n = int(input())
li = []

for i in range(n):
    x,y,k = map(int,input().split())

    if x<k and y<k:
        li.append(x*y)
    elif x>=k and y>=k:
        li.append(k**2)
    else:
        li.append(min(x,y)*k)

for i in li:
    print(i)