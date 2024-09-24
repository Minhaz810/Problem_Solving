t = int(input())
ans = []

for i in range(t):
    p1,p2,p3 = map(int,input().split())

    sum = p1+p2+p3

    if sum%2 == 1:
        ans.append(-1)
    else:
        res = min(p1+p2,sum//2)
        ans.append(res)

for i in ans:
    print(i)