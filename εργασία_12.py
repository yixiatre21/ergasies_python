file = open("project_12_ascii.txt", "r")
file_text = file.readlines()


def mirrorChar(num):
    mirror = 255 - num
    return mirror


anum = []
nnum = []

for text in file_text:
    for letter in text:
        anum.append(ord(letter))
        
for num in anum:
    print(chr(num), end = "")

anum.reverse()

for num in anum:
    nnum.append(mirrorChar(num))

print("\n")

for num in nnum:
    print(chr(num), end = "")