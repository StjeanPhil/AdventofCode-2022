import os 
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
file = open(file_path, "r")
data=file.readlines()
print("Problem 1: ")
for n1 in data:
    for n2 in data:
        if(int(n1)+int(n2)==2020):
            print(int(n1)*int(n2))

print("Problem 2: ")
for n1 in data:
    for n2 in data:
        for n3 in data:
            if(int(n1)+int(n2)+int(n3)==2020):
                print(int(n1)*int(n2)*int(n3))