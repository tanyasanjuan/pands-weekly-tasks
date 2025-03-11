# This program outputs whether or not today is a weekday.
# Author Tanya San Juan

# To determine if today is a weekday, we need to import the datetime module.
# Information on datetime module: https://docs.python.org/3/library/datetime.html

import datetime 

today = datetime.datetime.today().weekday()
# weekday() method returns the day of the week as an integer, Monday is 0 and Sunday is 6.
if today < 5:
    print ('Yes, unfortunately today is a weekday.')
else:
    print ('It is the weekend, yay!')

# References:
# https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,)%20to%206%20(Sunday).
# https://campus.datacamp.com/es/courses/working-with-dates-and-times-in-python/dates-and-calendars?ex=1