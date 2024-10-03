n,t = map(int,input().split())

li = list(map(int,input().split()))[:n]

current_cell = 0
for i in range(len(li)):
    current_cell+=li[current_cell]
    if current_cell == t-1:
        print("YES")
        break
    elif current_cell>t-1:
        print('NO')
        break
    else:
        continue