t = int(input())
ans = []

for i in range(t):
    n = int(input())

    p = list(map(int,input().split()))

    count = 0
    for i in p:
        bfi = p[i-1]
        bfii = p[bfi-1]
        if i == bfii:
            count = 2
            break
        else:
            count = 3
    
    ans.append(count)

for i in ans:
    print(i)