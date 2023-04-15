# this code takes the index of @
def indexOfAt(lines):
    for email in lines:
        for i in range(len(email)):
            if email[i] == "@":
                print(email.strip(), i)


ss_num = open("emailAddress.txt", "r")
indexOfAt(ss_num.readlines())
ss_num.close()