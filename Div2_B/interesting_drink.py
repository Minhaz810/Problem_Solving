n = int(input())
ans = []
li = []

li = list(map(int,input().split()))

li = sorted(li)
d = int(input())
for i in range(d):
    c = int(input())
    l = 0
    r = len(li)-1

    while(l<=r):
        mid = (l+r)//2
        if li[mid] <=c:
            l = mid+1
        else:
            r = mid-1
    ans.append(r+1)
for i in ans:
    print(i)