import os 
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
file = open(file_path, "r").readlines()
duplicates=[]
priority=0
print("Problem 1: ")
for line in file:
    #add strip() for line
    strippedline=line.strip()
    first= strippedline[:len(line)//2]
    second = strippedline[len(line)//2:]
    for letter in first:
        if letter in second:
            duplicates.append(letter)
            break

for letter in duplicates:
    if(letter.isupper()):
        currPrio=ord(letter)-65+27
    else:
        currPrio=ord(letter)-97+1
    priority+=currPrio
    print(letter,currPrio)
print(priority)

print("Problem 2: ")
badges=[]
priority=0
for i in range(0,len(file),3):
    elf1=file[i].strip()
    elf2=file[i+1].strip()
    elf3=file[i+2].strip()
    for letter in elf1:
        if(letter in elf2):
            if(letter in elf3):
             badges.append(letter)
             break
            
for letter in badges:
    if(letter.isupper()):
        currPrio=ord(letter)-65+27
    else:
        currPrio=ord(letter)-97+1
    priority+=currPrio
    print(letter,currPrio)
print(priority)


