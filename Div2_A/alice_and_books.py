t = int(input())

ans = []

for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))

    maximum = 0

    for i in range(len(li)-1):
        if li[i]>maximum:
            maximum = li[i]
    
    ans.append(maximum+li[len(li)-1])

for i in ans:
    print(i)

    