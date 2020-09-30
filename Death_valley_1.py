import csv
from datetime import datetime

open_file= open("death_valley_2018_simple.csv", "r")

csv_file= csv.reader(open_file, delimiter=",")

header_row= next(csv_file)
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




for row in csv_file:
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


import matplotlib.pyplot as plt

fig= plt.figure()

plt.plot(dates, highs, c="red",alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.title("Daily high and low temperatures- 2018\nDeath Valley", fontsize=16)
plt.xlabel("", fontsize=12)


plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha=0.1)


fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

plt.show()


