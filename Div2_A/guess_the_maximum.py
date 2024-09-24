t =int(input())
ans = []

for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]

    max_array = []
    for i in range(len(li)-1):
        max_array.append(max(li[i],li[i+1]))

    ans.append(min(max_array)-1)

for i in ans:
    print(i)

    
    