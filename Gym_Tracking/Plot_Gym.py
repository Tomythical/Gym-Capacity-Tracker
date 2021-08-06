import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
import pandas as pd
import numpy as np
import datetime


x= []

with open(f"/Users/ThomasMatheickal/Projects/Gym_Tracking/Data/{time.strftime('%d-%m-%y')}.txt", "r") as output:
    x = [line.strip() for line in output]

y = np.loadtxt("/Users/ThomasMatheickal/Projects/Gym_Tracking/Data/19-04-21.dat")
date = time.strftime('%d')
month = time.strftime('%m')
customdate = datetime.datetime(2021, int(month), int(date), 00, 00)
# for i in range(0,len(y)*5,5):
#     x.append(customdate + datetime.timedelta(minutes=i))

x2 =[]
# for times in x:
#     x2.append(datetime.date.fromisoformat(times))
# fig, ax = plt.subplots()
# myFmt = mdates.DateFormatter('%H:%M')
# ax.xaxis.set_major_formatter(myFmt)
# plt.plot(x2,y)
# fig.autofmt_xdate()
# plt.show()

p = datetime.date(2002, 12, 4).isoformat()
print(p)