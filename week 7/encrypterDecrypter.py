# this code encrypts / decrypts

def encrypter(file1, converter):
    fileOpened = False
    while not fileOpened:
        try:
            with open(file1, "r") as toBeEncrypted:
                temp = ""
                fileOpened = True
                for line in toBeEncrypted:
                    for character in line:
                        if character.lower() in converter:
                            temp += converter[character.lower()]
                        else:
                            temp += character
                with open("d.txt", "w") as encrypted:
                    encrypted.write(temp)
        except:
            print("File not found")
            break

def decrypter(file1, converter):
    fileOpened = False
    while not fileOpened:
        try:
            with open(file1, "r") as toBeDecrypted:
                temp = ""
                fileOpened = True
                for line in toBeDecrypted:
                    for character in line:
                        if character.lower() in converter:
                            temp += converter[character.lower()]
                        else:
                            temp += character
                with open("e.txt", "w") as decrypted:
                    decrypted.write(temp)
        except:
            print("File not found")
            break

allLetters = "abcdefghijklmnopqrstuvwxyz"
encrypterDict = {}
decrypterDict = {}
j = 0

while True:
    fileName = input("Enter filename: ")
    choice = input("Want to encrypt(e) / decrypt(d)")
    shiftnumber = int(input("What is the shift number?"))
    if shiftnumber > 26:
        shiftnumber %= 26
    for i in range(len(allLetters)):
        if shiftnumber + i < 26:
            encrypterDict[allLetters[i]] = allLetters[i + shiftnumber]
        else:
            encrypterDict[allLetters[i]] = allLetters[j]
            j += 1
    print(encrypterDict)


    for k, v in encrypterDict.items():
        decrypterDict[v] = k
    if choice.lower() == "e":
        encrypter(fileName, encrypterDict)
        break
    elif choice.lower() == "d":
        decrypter(fileName, decrypterDict)
        break
    else:
        print("Please enter e to encrypt or d to decrypt")
        continue