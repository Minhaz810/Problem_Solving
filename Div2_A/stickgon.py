t = int(input())
ans = []

for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]

    hashmap = {}

    for i in li:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    
    count = 0
    for key,value in hashmap.items():
        count+= (value//3)
    ans.append(count)

for i in ans:
    print(i)