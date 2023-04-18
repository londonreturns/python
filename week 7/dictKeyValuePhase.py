allLetters = "abcdefghijklmnopqrstuvwxyz"
encrypterDict = {}
decrypterDict = {}
phase = 29
j = 0
if phase > 26:
    phase %= 26
for i in range(len(allLetters)):
    if i < len(allLetters) - phase:
        encrypterDict[allLetters[i]] = allLetters[i+phase]
    else:
        encrypterDict[allLetters[i]] = allLetters[j]
        j += 1

for k,v in encrypterDict.items():
    decrypterDict[v] = k