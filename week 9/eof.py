try:
    string = input()
    print(string)
except EOFError:
    print("no data provided to input function")