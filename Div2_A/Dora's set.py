n = int(input())

li = []

for i in range(n):
    l,r = map(int,input().split())
    odd_count = 0
    for i in range(l,r+1):
        if i%2 == 1:
            odd_count+=1
    
    li.append((odd_count//2))

for i in li:
    print(i)