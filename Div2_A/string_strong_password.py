n = int(input())

li = []
for i in range(n):
    s = input()
    res = ''
    i = 1

    while(i<len(s)):
        if s[i] == s[i-1]:
            break
        i+=1
    
    if i == len(s):
        if s[len(s)-1] == 'a':
            res = s+'b'
        elif s[len(s)-1] == 'b':
            res = s+'a'
        else:
            res = s+'a'
    else:
        if s[i] == 'a':
            res = s[:i]+'b'+s[i:]
        elif s[i] == 'b':
            res = s[:i]+'a'+s[i:]
        else:
            res = s[:i]+'a'+s[i:]

    li.append(res)

for i in li:
    print(i)
    