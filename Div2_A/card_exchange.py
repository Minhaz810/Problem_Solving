t =int(input())
ans = []

for i in range(t):
    n,k = map(int,input().split())
    li = list(map(int,input().split()))

    hashmap = {}

    for i in li:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    

    i = 0
    for key,value in hashmap.items():
        if hashmap[key]>=k:
            ans.append(k-1)
            break
        i+=1
    if i == len(hashmap):
        ans.append(len(li))

for i in ans:
    print(i)
