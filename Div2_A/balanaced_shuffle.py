
s = input()

s2 = ""

prefix_sum = 0

hashmap = {0:[0]}
for i in range(1,len(s)):
    if s[i-1] == "(":
        prefix_sum+=1
    else:
        prefix_sum-=1

    if prefix_sum in hashmap:
        hashmap[prefix_sum].append(i)
    else:
        hashmap[prefix_sum] = [i]

s2 = ""

for i in hashmap:
    hashmap[i] = sorted(hashmap[i],reverse= True)

for i in hashmap:
    for j in hashmap[i]:
        s2+=s[j]
print(s2)


    


        