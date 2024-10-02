t = int(input())
ans =[]

for i in range(t):
    n,k = map(int,input().split())
    if(k==1):
        ans.append(n)
    else:
        power = 0
        while((n-k**power)>0):
            power+=1
        if n-k**power == 0:
            ans.append(1)
        else:
            count=0
            while power >=0:
                count+=((n%k**power)//(k**(power-1)))
                n = n%(k**(power-1))
                power-=1

            ans.append(count)

for i in ans:
    print(int(i))

    