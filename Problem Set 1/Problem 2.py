s = 'azcbobobegghakl'
a = 0
b = a + 3
num = 0
while(b <= len(s)):
    if(s[a:b] == "bob"):
        num = num + 1
    a = a + 1
    b = b + 1
print("Number of times bob occurs is: ", str(num))