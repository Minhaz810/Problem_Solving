n = int(input())
li = list(map(int,input().split()))

hashmap  = {4:0,3:0,2:0,1:0}

for i in li:
    hashmap[i]+=1

if hashmap[1] <= hashmap[3]:
    hashmap[1] = 0
else:
    hashmap[1]-=hashmap[3]

if hashmap[2]%2 == 0:
    hashmap[2] = hashmap[2]//2
else:
    hashmap[2] = hashmap[2]//2+1
    hashmap[1] -= 2

if hashmap[1]<=0:
    hashmap[1] = 0
else:
    if hashmap[1]%4 == 0:
        hashmap[1] = hashmap[1]//4
    else:
        hashmap[1] = hashmap[1]//4+1

count = 0
for i in hashmap:
    count+=hashmap[i]

print(count)