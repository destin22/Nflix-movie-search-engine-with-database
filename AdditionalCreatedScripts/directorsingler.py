f = open("directorsTable.csv", encoding='utf-8', errors='ignore')
i=0
line = f.readlines()
for y in line:
    names = y.split(',')
    newstr = names[0] +','+ names[1].strip()
    print(newstr + '\n')
    #write the updated strings to a new file
    g = open("directorsTableUpdated.csv", "a", encoding='utf-8', errors='ignore')
            #add a new line character for mysql
    g.write(newstr + '\n')
    g.close