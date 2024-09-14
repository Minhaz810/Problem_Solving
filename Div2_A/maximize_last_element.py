n = int(input())

li = []
for i in range(n):
    k = int(input())
    el_2 = []
    el = list(map(int,input().split()))
    
    for i in range(len(el)):
        if i%2 == 0:
            el_2.append(el[i])
    li.append(max(el_2))
            

print("Output")                
for i in li:
    print(i)