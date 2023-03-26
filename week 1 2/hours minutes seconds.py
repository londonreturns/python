#calculate hours, minutes, seconds

#assign values
total_seconds = 13445

#calculate hours, minutes, seconds
hours = int(total_seconds / 3600)
remaining_seconds = total_seconds - hours  * 3600
minutes = int(remaining_seconds / 60)
#remaining_seconds = total_seconds - minutes  * 60
seconds = total_seconds % 60

print(total_seconds, "Seconds is ", hours, "hours, ", minutes, "minutes, and ", seconds, "seconds")
