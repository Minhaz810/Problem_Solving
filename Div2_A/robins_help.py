t = int(input())
ans = []

for i in range(t):
    n,k = map(int,input().split())

    li = list(map(int,input().split()))

    robin_gold = 0
    poor_count = 0
    for i in li:
        if i>=k:
            robin_gold+=i
        if robin_gold>0 and i == 0:
            poor_count+=1
            robin_gold-=1
    ans.append(poor_count)

for i in ans:
    print(i)
