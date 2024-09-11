n = int(input())

li = []
for i in range(n):
    x,y,d = map(int,input().split())

    x_steps = int((x+d-1)/d)
    y_steps = int((y+d-1)/d)

    if y_steps>x_steps:
        total_steps = 2*y_steps
    elif x_steps > y_steps:
        total_steps = 2*x_steps -1
    else:
        total_steps = 2*x_steps

    li.append(total_steps)

for i in li:
    print(i)