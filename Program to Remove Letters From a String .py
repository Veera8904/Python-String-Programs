#using replace()

s = "hello world"
s = s.replace("l", "")
print(s)



#using for loop

s = "hello world"
s1 = ""

for c in s:
    if c != "o":
        s1 += c

print(s1)