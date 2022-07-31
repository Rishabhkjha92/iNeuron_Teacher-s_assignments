import datetime as dt
import click

click.clear()
# d = str(dt.date)
# t = dt.time
# z = dt.timezone
cur_time = dt.datetime.now()
y = cur_time.year
m = cur_time.month
d = cur_time.day
h = cur_time.hour
m = cur_time.minute
s = cur_time.second
micro = cur_time.microsecond

# print("Currently :\n","Date is :\t",dt,"\nTime is :\t",t,"\nTimeZone is :\t",z,"\nand\nCurrent Time is :\t",cur_time)

print("Current \nYear :\t",y,"\t Month :\t",m,"\t Date :\t",d,"\tHour :\t",h,"\t Minute :\t",m)