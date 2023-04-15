# this codes formats error message

def errorMessage(message):
    tempMessage = ""
    for character in message:
        if character == " " or character == "*":
            continue
        else:
            tempMessage += character
    print(tempMessage)

err_mesg = open("errorMessage.txt", "r")
errorMessage(err_mesg.readline())
err_mesg.close()