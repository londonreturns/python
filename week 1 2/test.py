# defining improved_average( )  function
def improved_average (num1, num2, num3, num4, num5):
    # importing statistics library
    import statistics
    # store all numbers in a list
    num_list = [num1, num2, num3, num4, num5]
    mean = statistics.mean(num_list)
    median = statistics.median(num_list)
    mode = statistics.mode(num_list)
    return mean, median, mode


meanval, medianval, modeval = improved_average(5, 5, 4, 7, 9)

print("Mean is ", meanval, "\nMedian is ", medianval, "\nMode is ", modeval)
