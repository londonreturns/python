"""this code calculates returns the average temperature
over the weekend for the weekly temperatures given"""

def get_weekend_average_temp(temps):
    sum = 0
    for temperature in temps.values():
        sum += temperature
    average = format(sum / len(temps),".2f")
    return average

allTemps = {
    "Sunday":15,
    "Monday":16,
    "Tuesday":17,
    "Wednesday":15,
    "Thursday":14,
    "Friday":20,
    "Saturday":21
}
print(get_weekend_average_temp(allTemps))