s = input()
n = int(input())
ans = []
for i in range(n):
    l,r = map(int,input().split())
    
    count = 0
    for i in range(l-1,r-1):
        if s[i] == s[i+1]:
            count+=1

    ans.append(count)

for i in ans:
    print(i)