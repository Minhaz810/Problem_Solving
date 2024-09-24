t = int(input())

ans = []

for i in range(t):
    n = int(input())

    vowel = ['a','e','i','o','u']

    s = ""

    if n<=len(vowel):
        for i in range(n):
            s+=vowel[i]
    else:
        temp = vowel*(n//5)
        for i in range(n%5):
            temp.append(vowel[i])
        
        temp = sorted(temp)
        for i in range(len(temp)):
            s+=temp[i]
        
    
    ans.append(s)

for i in ans:
    print(i)
        