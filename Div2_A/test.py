n = int(input())
li = []
for i in range(n):
    k = int(input())
    inp = list(map(int,input().split()))
    
    inp = sorted(inp)

    if k == 1:
        li.append(inp[0])
    else:
        li.append(inp[k//2])

for i in li:
    print(i)