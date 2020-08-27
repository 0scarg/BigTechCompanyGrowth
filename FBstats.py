#Facebook Data from NASDAQ

import pandas
import matplotlib.pyplot as plt

filename = "FB-NASDAQ-data.csv"
fb= pandas.read_csv(filename)
print(fb)

highs = fb.High
<<<<<<< HEAD
print("")
=======
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e
print("High values from January 2nd to August 25th:")
print(highs)

lows = fb.Low
<<<<<<< HEAD
print("")
=======
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e
print("Low values from January 2nd to August 25th")
print(lows)

high_august25 = highs[0]
<<<<<<< HEAD
print("")
=======
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e
print("High Value on August 25th, 2020:")
print(high_august25)

low_august25 = lows[0]
<<<<<<< HEAD
print("")
=======
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e
print("Low value on August 25th, 2020")
print(low_august25)

Date = fb.Date

plt.plot(Date,highs)

<<<<<<< HEAD
plt.xlabel("Date")
plt.ylabel("High Values")
=======
plt.xlabel("High Values")
plt.ylabel("Date")
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e
plt.title("High Values from January 2nd to August 25")

plt.show()