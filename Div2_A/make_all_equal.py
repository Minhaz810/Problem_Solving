n = int(input())

li = []
for i in range(n):
    k = int(input())
    arr = list(map(int,input().split()))

    hashmap = {}

    for i in arr:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i] = 1
    
    max_occurance = 1

    for i in hashmap:
        if hashmap[i]>max_occurance:
            max_occurance = hashmap[i]

    li.append(len(arr)-max_occurance)

for i in li:
    print(i)