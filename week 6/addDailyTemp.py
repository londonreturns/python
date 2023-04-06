# add daily temp

def add_daily_temp(avgDailyTemp, temperature, dayOfWeek):
    isNotDayCount = 0
    for eachDay in avgDailyTemp.keys():
        if not eachDay.lower() == dayOfWeek.lower():
            isNotDayCount += 1
    if isNotDayCount == len(avgDailyTemp):
        avgDailyTemp[dayOfWeek] = temperature
    return avgDailyTemp

averageDailyTemperature = {"Sunday": 25.0,
                           "Monday": 26.2,
                           "Tuesday": 20.6,
                           "Saturday": 15.2}  # initializing
newDay = input("Enter a day: ")  # take input from user
newTemp = float(input("Enter temperature : "))

averageDailyTemperature = add_daily_temp(averageDailyTemperature, newTemp, newDay)

print(averageDailyTemperature)