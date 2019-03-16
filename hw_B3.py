f = open('rosalind_hamm.txt', 'r')

    


str1 = f.readline()
str2 = f.readline()
counter = 0
for i in range (len(str2)):
    if str1[i] != str2[i]:
        counter += 1
print(counter)
f.close()
    
                            

            
