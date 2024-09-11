n = int(input())
li = []

for i in range(n):
    l,r = map(int,input().split())
    L,R = map(int,input().split())

    il = max(l,L)
    ir = min(r,R)
    ans = ir-il
    if il>ir:
        li.append(1)
    else:
        if min(l,L)<il:
            ans+=1
        if max(r,R)>ir:
            ans+=1
        li.append(ans)
    


for i in li:
    print(i)
