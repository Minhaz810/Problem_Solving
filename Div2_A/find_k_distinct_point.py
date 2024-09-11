n = int(input())
li = []
for i in range(n):
    k = int(input())
    s = input()

    hashmap = {}
    for i in s:
        if i!= "?":
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        else:
            continue

    result = 0
       
    for i in hashmap:
        result+= min(hashmap[i],k)
    li.append(result)
    


for i in li:
    print(i)
