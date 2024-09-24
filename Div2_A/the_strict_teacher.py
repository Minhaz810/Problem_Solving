n = int(input())

ans = []

for i in range(n):
    cell,teacher,query = map(int,input().split())

    t1,t2 = map(int,input().split())

    d = int(input())
    count = 0

    if (t1>d and t2>d):
        ans.append(min(t1,t2)-d)
    elif (t1<d and t2<d):
        ans.append(max(t1,t2)-d)
    else:
        if t1>t2:
            if abs(t1-d)>abs(t2-d):
                while t1>d:
                    t1-=1
                    d+=1
                    t2+=1
                    count+=1
                while t2<d:
                    t2+=1
                    d-=1
                    count+=1
            else:
                while t2<d:
                    t2+=1
                    d-=1
                    t1-=1
                    count+=1
                while t1>d:
                    t1-=1
                    d+=1
                    count+=1

        else:
            if abs(t2-d)>abs(t1-d):
                while t2>d:
                    t2-=1
                    d+=1
                    t1+=1
                    count+=1
                while t1<d:
                    t1+=1
                    d-=1
                    count+=1
            else:
                while t1<d:
                    t1+=1
                    d-=1
                    t2-=1
                    count+=1
                while t2>d:
                    t2-=1
                    d+=1
                    count+=1


for i in ans:
    print(i)