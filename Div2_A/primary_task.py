n = int(input())

li = []
for i in range(n):
    n = int(input())
    s = str(n)
    p = s[2:]
    k = s[:2]

    if len(s)<3:
        li.append("NO")
    elif k == "10" and p[0]!="0" and int(p)>=2:
        li.append("YES")
    else:
        li.append("NO")

for i in li:
    print(i)