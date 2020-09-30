import csv
from datetime import datetime

open_file= open("death_valley_2018_simple.csv", "r")

deathvalley_file= csv.reader(open_file, delimiter=",")

header_row= next(deathvalley_file)
'''
print(header_row)

for index, column_header in enumerate(header_row):
    print(index,column_header)
'''

lows=[]
highs = []
dates = []


#x= datetime.strptime('2018-07-01','%Y-%m-%d')
#print(x)
for row in deathvalley_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date= datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        lows.append(int(row[5]))
        highs.append(int(row[4]))
        dates.append(current_date)



open_file= open("sitka_weather_2018_simple.csv", "r")

sitka_file= csv.reader(open_file, delimiter=",")

header_row= next(sitka_file)
'''
print(header_row)
for index, column_header in enumerate(header_row):
    print(index,column_header)
'''
low=[]
high = []
date = []

#x= datetime.strptime('2018-07-01','%Y-%m-%d')
#print(x)

for row in sitka_file:
    low.append(int(row[6]))
    high.append(int(row[5]))
    the_date= datetime.strptime(row[2],'%Y-%m-%d')
    date.append(the_date)
import matplotlib.pyplot as plt

#fig, ax = plt.subplots(2)

#fig1= plt.figure()

#ax[1]= plt.plot(date, high, c="red",alpha=0.5)
#ax[0]= plt.plot(date, low, c="blue", alpha=0.5)
plt.title("Daily high and low temperatures- 2018\nDeath Valley & Sitka, Alaska", fontsize=16)
plt.plot(date, high, c="red",alpha=0.5)
plt.plot(date, low, c="blue", alpha=0.5)


plt.fill_between(date, high, low, facecolor= 'blue', alpha=0.1)

#fig1.autofmt_xdate()

plt.ylabel("Temp (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

#fig2= plt.figure()

plt.plot(dates, highs, c="red",alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

#plt.title("Daily high and low temperatures- 2018\nDeath Valley & Sitka, Alaska", fontsize=16)
plt.xlabel("", fontsize=12)

plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha=0.1)

#fig2.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)
plt.show()

