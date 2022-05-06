import datetime

# get today
dt_today = datetime.datetime.today().date()
print(f'Today is {dt_today} \n')

# create new date
date = datetime.date(2022, 10, 0o1)
print(f'Created date {date} \n')

# acess atributes to date
year = date.year
month = date.month
day = date.day
print(f'Year: {year} - Month: {month} - Day: {day} \n')

# diif days
diff_days = date - dt_today
print(f'Diff is {diff_days} days \n')

# add days
add_days = dt_today + datetime.timedelta(days=30)
print(f'added 30 days {dt_today} para {add_days}')

# remove days
remove_days = dt_today + datetime.timedelta(days=30)
print(f'removed 30 days {dt_today} para {remove_days}')
