f = open("precastWshowid.csv", encoding='utf-8', errors='ignore')
i=0
line = f.readlines()
for y in line:
    #print(y)
    names = y.split(',')
    castid = names[0]
    for x in names:
        #this is so the castid doesnt append itself to itself
        if names.index(x) != 0:
            newstr = x.strip()
            newstr = castid +','+ newstr
            #print(newstr)
            #write the updated strings to a new file
            g = open("castupdatedWshowid.csv", "a", encoding='utf-8', errors='ignore')
            #add a new line character for mysql
            g.write(newstr+'\n')
            g.close