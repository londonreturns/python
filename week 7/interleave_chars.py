#this code interleaves two lines

def interleave_chars(line1, line2):
    temp = ""
    for i in range(min(len(line1), len(line2))):
        temp += line1[i] + line2[i]
    if len(line1) > len(line2):
        temp += line1[len(line2):]
    elif len(line2) > len(line1):
        temp += line2[len(line1):]
    return temp






file1 = (open("interleave_chars.txt", "r"))
line1 = file1.readline().strip()
line2 = file1.readline().strip()
print(interleave_chars(line1, line2))
file1.close()