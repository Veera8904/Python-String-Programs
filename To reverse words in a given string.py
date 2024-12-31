# To reverse words in a given string

string = "my name is veerendra"
s = string.split()[::-1]
l = []
for i in s:
	l.append(i)
print(" ".join(l))
