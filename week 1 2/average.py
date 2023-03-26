#defining average function
def average(sub1, sub2, sub3, sub4, sub5):
    """this function calculates average"""
    avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
    return avg

#display docstring
print(average.__doc__)


#assigning values
sub1 = 1
sub2 = 1
sub3 = 1
sub4 = 1
sub5 = 1

#display output
averageMarks = average(sub1, sub2, sub3, sub4, sub5)
print("your average is ", averageMarks)
