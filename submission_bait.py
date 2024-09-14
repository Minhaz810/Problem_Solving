n = int(input())
ans = []
for i in range(n):
    k = int(input())

    li  = list(map(int,input().split()))

    hashmap = {}

    for i in li:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i] = 1

    for index,key in enumerate(hashmap):
        if hashmap[key]%2 != 0:
            ans.append("YES")
            break
        if len(hashmap) == index+1:
            ans.append("NO")
        

for i in ans:
    print(i)
