str = "wooow"
s = list(str)
"""for i,v in enumerate(s):
    print(i,v)
"""
l = len(s)
# print(l)
flag = True
for i in range(0, int(l/2)):
    if not s[i] == s[l-i-1]:
        flag = False
        break
if flag:
    print("Pallindrome")
else:
    print("Not s pallindrome")

# print(s)
