t = int(input())
ans = []

for i in range(t):
    n,m,k = map(int,input().split())

    if k >= n-1:
        ans.append("NO")
    else:
        if m == 1:
            ans.append("NO")
        elif m >= 2:
            if k<(n//2):
                ans.append("YES")
                print("OYE")
            else:
                ans.append("NO")
                print("BYE")
        else:
            ans.append("YES")
        

for i in ans:
    print(i)
    