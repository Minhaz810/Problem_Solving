t = int(input())
ans = []

for i in range(t):
    n = int(input())
    
    li = list(map(int,input().split()))

    li_s = sorted(li)

    if li == li_s:
        ans.append("Yes")
    else:
        for i in li:
            f = li.pop(0)
            li.append(f)
            if li == li_s:
                break
        if li == li_s:
            ans.append("Yes")
        else:
            ans.append("No")

for i in ans:
    print(i)
