# this code checks if ss has any non digits

def hasNonDigits(lines):
    sum = ""
    for line in lines:
        if line.strip().isdigit():
            print("Does not contain any non digits")
        else:
            print("Contains non digits")

ss_num = open("ss_num.txt", "r")
hasNonDigits(ss_num.readlines())
ss_num.close()