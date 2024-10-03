# s = input()
# n = int(input())
# ans = []
# for i in range(n):
#     l,r = map(int,input().split())
    
#     count = 0
#     for i in range(l-1,r-1):
#         if s[i] == s[i+1]:
#             count+=1

#     ans.append(count)

# for i in ans:
#     print(i)
"""Time limit exceeded"""

s = input()
n = int(input())
ans = []

sum_array = [0]
count = 0
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count+=1
    sum_array.append(count)

sum_array.append(count)
print(sum)

for i in range(n):
    l,r = map(int,input().split())
    print(sum_array[r-1]-sum_array[l-1])
