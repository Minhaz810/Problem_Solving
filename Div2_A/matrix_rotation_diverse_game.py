n = int(input())
mat_b_list = []
for i in range(n):
    m,n = map(int,input().split())

    mat_a = []
    for i in range(m):
        col = list(map(int,input().split()))[:n]
        if m == 1 and n == 1:
            mat_a.append([-1])
        else:
            if m == 1:
                col_1 = col.pop(0)
                col.append(col_1)
            mat_a.append(col)
    
    row_1 = mat_a.pop(0)
    mat_a.append(row_1)

    mat_b_list.append(mat_a)


for mat in mat_b_list:
    for row in mat:
        for col in row:
            print(col,end=" ")
        print()

                