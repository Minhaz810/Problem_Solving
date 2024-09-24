t = int(input())
li =[]
for i in range(t):
    n,k = map(int,input().split())

    ans = 0

    while(n>1):
        ans+=1
        n-= (k-1)
        print(n)
    li.append(ans)

for i in li:
    print(i)

