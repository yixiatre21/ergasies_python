file = open("project_9_ascii.txt", "r")
file_text = file.readlines()
file_text[0] = file_text[0].upper()

odd = []
flag = []
temp = 0

for text in file_text:
    for letter in text:
        temp = ord(letter)
        if temp % 2 != 0:
            odd.append(temp)

for i in range(65, 91):
    flag.append(False)
    for letter in odd:
        if i == letter:
            flag[i - 65] = True

for i in range(65, 91):
    if (flag[i - 65]):
        print("\n[", chr(i), "]: ", end= "")
        for letter in odd:
            if i == letter:
                print("*", end = "")