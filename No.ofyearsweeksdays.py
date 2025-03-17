no_of_days=int(input())

years=no_of_days//365
rem=no_of_days%365
print("Number of years(365):" +str(years))

weeks=rem//7
rem=rem%7
print("Number of weeks (7):" + str(weeks))

days=rem
print("Number of days(1):" + str(days))
