def is_palindrome(string):
    if len(string) == 1:
        return True
    if string[0] == string[-1]:
        rest = string[1:-1]
        return is_palindrome(rest)
    else:
        return False
    
    
    
user_input = input('enter a string: ')

print(is_palindrome(user_input))
