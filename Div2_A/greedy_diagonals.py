t = int(input())

li = []
for i in range(t):
    n,k = map(int,input().split())

    count = 0
    if k == 0:
        li.append(0)
    else:
        k = k-n
        i = 1

        while k>0:
            if k>n-i:
                count+=2
                k -= 2*(n-i)
                i+=1
            else:
                count+=1
                k-=(n-i)
                i+=1
        li.append(count+1)
         
for i in li:
    print(i)
        
    
    