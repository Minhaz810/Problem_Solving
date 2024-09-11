n = int(input())

res = []
for i in range(n):
    k = int(input())
    li = list(map(int,input().split()))

    odd_count = 0
    even_count = 0
    for i in li:
        if i%2 == 1:
            odd_count+=1
        else:
            even_count+=1
    
    if odd_count == len(li) or even_count == len(li):
        res.append(0)
    else:
        maximum = max(li)
        if maximum%2 == 1:
            res.append(even_count)
        else:
            res.append(even_count+1)

for i in res:
    print(i)


