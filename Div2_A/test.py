s = "aabc"
i = 1
while(i<len(s)):
    if s[i] == s[i-1]:
        break
    i+=1

print(i)