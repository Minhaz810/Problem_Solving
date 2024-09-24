t = int(input())
li = []
for i in range(t):
    n,k = map(int,input().split())

    li.append(((n-1)*k)+1)

for i in li:
    print(i)

    