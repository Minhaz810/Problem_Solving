t = int(input())
ans = []

for i in range(t):
    n,k = map(int,input().split())

    leaves = 0

    start = n-k+1
    end = n

    odd_count = 0

    if start%2 == 0 and end%2 == 0:
        odd_count = (end-start)//2
    elif start%2 == 0 and end%2 != 0:
        odd_count = (end-start-1)//2 + 1
    elif start%2 != 0 and end%2 == 0:
        odd_count = (end-start-1)//2 + 1
    else:
        odd_count = (end-start)//2 + 1

    if odd_count%2 == 0:
        ans.append("YES")
    else:
        ans.append("NO")
        
for i in ans:
    print(i)