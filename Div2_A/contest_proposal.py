t = int(input())
ans = []

for i in range(t):
    n = int(input())

    li1 = list(map(int,input().split()))
    li2 = list(map(int,input().split()))

    i = 0
    j = 0
    count = 0
    while(j<len(li2)):
        if li1[i]<=li2[j]:
            i+=1
            j+=1
        else:
            count+=1
            j+=1
    ans.append(count)
for i in ans:
    print(i)

