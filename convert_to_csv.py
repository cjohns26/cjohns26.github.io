src = open("/home/cjohnson/Documents/FAR_KOMS.txt", encoding='utf-16')
dst = open("/home/cjohnson/Documents/FAR_KOMS.csv", "x")

for line in src:
    newline = ""
    # Loop through line
    for i in range(len(line)):
        # if character is not a space
        if(line[i] != ' '):
            newline += line[i]  
        # if character is a space
        if line[i] == ' ':
            # if next character is a space
            if line[i + 1] == ' ':
                # set a , instead
                newline += ','
                # for the rest of the string only add to new if not a space
                for l in range(i + 1, len(line)):
                    if line[l] != ' ':
                        newline += line[l]
                break
            # if next is not a space
            else:
                newline += line[i]

    dst.write(newline)

         
#print(line)   
#print(newline)       
                
    