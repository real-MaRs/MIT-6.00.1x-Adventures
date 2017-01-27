string1 = ''
string2 = ''
a = 0
for letter in range(len(s)-1):
    if(s[letter] <= s[letter+1]):
        string1 = s[a:letter + 1]
    else:
        if(len(string1) > len(string2)):
            string2 = string1
        string1 = ''
        a = letter + 1
    
print(string2)