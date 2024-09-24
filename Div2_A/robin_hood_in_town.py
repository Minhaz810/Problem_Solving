t = int(input())
ans = []

for i in range(t):
    n = int(input())

    li = list(map(int,input().split()))

    li = sorted(li)

    start = 0
    end = len(li)-1
    mid = (start+end)//2

    if n == 1 or n == 2:
        ans.append(-1)

    else:
        if len(li)%2 == 0:
            if sum(li)/(n*2) > li[mid+1]:
                ans.append(0)
            else:
                result = li[mid+1]*n*2-sum(li)+1
                ans.append(result)
        else:
            if sum(li)/(n*2) > li[mid]:
                ans.append(0)
            else:
                result = li[mid]*n*2-sum(li)+1
                ans.append(result)

for i in ans:
    print(i)