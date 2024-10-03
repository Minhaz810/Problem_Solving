n,t = map(int,input().split())

count = 0
while(n>0):
    if n<t:
        count +=n
    else:
        count +=t
    n-=t
    n+=1
    
print(count)
