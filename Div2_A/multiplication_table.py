n,m = map(int,input().split())

count = 0
for i in range(1,n+1):
    if m%i == 0 and m//i<=n:
        count+=1
    else:
        continue

print(count)
