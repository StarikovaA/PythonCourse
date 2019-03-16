with open('rosalind_revc.txt', 'r') as file:
                            a = file.read()
b = a.replace ("A", 'B')
c = b.replace ("T", 'A')
m = c.replace ('B', 'T')
q = m.replace ("C", 'O')
z = q.replace ('G', 'C')
s = z.replace ("O", "G")
newstr = ""
x = len (s)
i = 1
while i <= x :
    newstr = newstr + s[x - i]
    i = i + 1
print (newstr)
