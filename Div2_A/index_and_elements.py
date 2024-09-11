n = int(input())

result = []
for i in range(n):
    l,no = map(int,input().split())

    li = list(map(int,input().split()))
    li.sort()
    li2 =[]
    for i in range(no):
        c,l,r = input().split()
        l = int(l)
        r = int(r)

        last_index = len(li)-1
        if li[last_index]<l:
             maximum = li[last_index]
        elif r<li[last_index]:
                maximum = li[last_index] 
        else:
            if c == '+':
                 maximum = li[last_index]+1
                 li[last_index]+=1
            else:
                 maximum = li[last_index]-1
                 li[last_index]-=1

        li2.append(maximum)
    result.append(li2)

for i in result:
    for j in i:
        print(j, end=" ")
    print()
