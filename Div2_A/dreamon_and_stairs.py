n,t = map(int,input().split())
mn = n//2+n%2
if t>n:
    print(-1)
else:
    for i in range(mn,n+1):
        if i%t == 0:
            print(i)
            break
        else:
            continue

