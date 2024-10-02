n = int(input())
ans = []

for i in range(n):
    a = int(input())

    if 360%(180-a) == 0:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)

    

