#define name function
def name_function(name):
    """This function prints your name"""    
    print("Your name is ", name)

#input from user
print(name_function.__doc__)
name = input ("what is your name? ")
name_function(name)
    
