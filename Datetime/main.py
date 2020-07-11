import datetime
import pytz

today=datetime.date.today()

birthday=datetime.date(1990,5,22)

# .days mae sure we'll obtain only days and not hours
days_since_birth= (today- birthday).days
print(days_since_birth)

tdelta=datetime.timedelta(days=7)
print(today+tdelta)

print(today.day)
print(today.weekday())

print(datetime.time(7,10,20,15))
# datettime.date(y,m,d) 
#datetime.time(h,m,s,ms)
#datetime.datetime(y,m,d,h,m,s,ms)

#What time is it now in your current location?
time=datetime.datetime.now()
print(time)
#subtract 6 hours
tdelta=datetime.timedelta(hours=6)
print(time-tdelta)

# in my timezone
dtty=datetime.datetime.now(tz=pytz.UTC)
print(dtty.astimezone(pytz.timezone('US/Pacific')))

#for tz in pytz.all_timezones:
#  print(tz)

print(dtty.astimezone(pytz.timezone('Europe/Rome')))


#string formating with dates

print(dtty.strftime('%B,%d,%Y'))
today_f=dtty.strftime('%B,%d,%Y')
#to do the opposite 'March 09, 2019' for example inside the strptime('March 09, 2019','%B,%d,%Y')
print(dtty.strptime(today_f,'%B,%d,%Y'))

