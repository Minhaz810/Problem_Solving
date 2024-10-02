t = int(input())
ans = []
for i in range(t):
    n = int(input())
    s = input()[:n]
    removing_zeroes = ""
    for i in range(len(s)-1):
        if s[i] == '0' and s[i+1] == '0':
            continue
        else:
            removing_zeroes+=s[i]
    if s[len(s)-1] == '1':
        removing_zeroes+='1'
    else:
        removing_zeroes+='0'
    
    c0 = 0
    c1 = 0

    for i in removing_zeroes:
        if i == '0':
            c0+=1
        else:
            c1+=1
    if c1>c0:
        ans.append("Yes")
    else:
        ans.append("No") 
        
for i in ans:
    print(i)