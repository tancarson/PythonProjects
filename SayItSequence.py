seq = 1
string = str(seq)
print(string)
for i in range(0,30):
    count = 1
    newstring = ""
    for j in range(0,len(string)-1):
        if string[j] == string[j+1]:
            count += 1
        else:
            newstring += str(count) + string[j]
            count = 1
    newstring += str(count) + string[len(string)-1]
    string = newstring
    print(string)