n,m = map(int,input().split())

li = list(map(int,input().split()))[:n]

hashmap = {}
count_arr = []
count = 0
for i in range(len(li)-1,-1,-1):
    if li[i] in hashmap:
        pass
    else:
        hashmap[li[i]] = 1
        count+=1
    
    count_arr.append(count)

count_arr.reverse()

for i in range(m):
    l = int(input())
    print(count_arr[l-1])

