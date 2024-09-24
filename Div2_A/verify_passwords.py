t = int(input())
ans = []

for i in range(t):
    n = int(input())
    s1 = input()

    s2 = sorted(s1)

    s2 = "".join(s2)

    if s1 == s2:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)
    
