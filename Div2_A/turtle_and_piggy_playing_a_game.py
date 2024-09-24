t = int(input())
ans = []

for i in range(t):
    l,r = map(int,input().split())

    current = 1
    count = 0
    while current*2<=r:
        count+=1
        current*=2
    
    ans.append(count)

for i in ans:
    print(i)