n = int(input())
ans = []
for i in range(n):
    x,y = map(int,input().split())

    if y < -1:
        ans.append("NO")
    else:
        ans.append("YES")

for i in ans:
    print(i)
