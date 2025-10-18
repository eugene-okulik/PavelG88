import datetime


date = "Jan 15, 2023 - 12:05:33"

pyth_date = datetime.datetime.strptime(date, "%b %d, %Y - %H:%M:%S")
print(pyth_date)

print(pyth_date.strftime("%B"))
print(pyth_date.strftime("%d.%m.%Y, %H:%M"))
