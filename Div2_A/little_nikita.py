t = int(input())
ans = []

for i in range(t):
    n,m = map(int,input().split())

    if m > n:
        ans.append("No")
    else:
        if (m-n)%2 == 0:
            ans.append("Yes")
        else:
            ans.append("No")

for i in ans:
    print(i)