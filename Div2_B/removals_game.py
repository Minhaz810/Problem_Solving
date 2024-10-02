t = int(input())
ans = []
for i in range(t):
    n = int(input())
    li1 = list(map(int,input().split()))
    li2 = list(map(int,input().split()))
    flag = False

    if li1 == li2:
        ans.append("Bob")
    elif li1 == li2[::-1]:
        ans.append("Bob")
    else:
        ans.append("Alice")

for i in ans:
    print(i)
        
