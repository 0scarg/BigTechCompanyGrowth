#Facebook Data from NASDAQ

import pandas
import matplotlib.pyplot as plt

filename = "FB-NASDAQ-data.csv"
fb= pandas.read_csv(filename)
print(fb)

highs = fb.High
print("High values from January 2nd to August 25th:")
print(highs)

lows = fb.Low
print("Low values from January 2nd to August 25th")
print(lows)

high_august25 = highs[0]
print("High Value on August 25th, 2020:")
print(high_august25)

low_august25 = lows[0]
print("Low value on August 25th, 2020")
print(low_august25)

Date = fb.Date

plt.plot(Date,highs)

plt.xlabel("High Values")
plt.ylabel("Date")
plt.title("High Values from January 2nd to August 25")

plt.show()