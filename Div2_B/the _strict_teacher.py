t = int(input())
ans = []

for i in range(t):
    m,n,q = map(int,input().split())
    t1,t2 = map(int,input().split())
    d = int(input())

    if d<t1 and d<t2:
        ans.append(min(t1,t2)-1)
    elif d>t1 and d>t2:
        ans.append(m-max(t1,t2))
    else:
        mid = (t1+t2)//2
        distance_from_mid_t1 = abs(mid-t1)
        distance_from_mid_t2 = abs(mid-t2)

        if distance_from_mid_t1<distance_from_mid_t2:
            ans.append(distance_from_mid_t1)
        else:
            ans.append(distance_from_mid_t2)

for i in ans:
    print(i)