#Apple Data from NASDAQ

import pandas 
import matplotlib.pyplot as plt

filename = "Apple-NASDAQ-data.csv"
df = pandas.read_csv(filename)
print(df)

highs = df.High
<<<<<<< HEAD
print("")
=======
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e
print("High values from January 2nd to August 25th:")
print(highs)

lows = df.Low
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
print("High value on August 25th, 2020")
print(high_august25)

low_august25 = lows[0]
<<<<<<< HEAD
print("")
=======
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e
print("Low value on August 25th, 2020")
print(low_august25)

Date = df.Date

plt.plot(Date,highs)
plt.xlabel("Date")
plt.ylabel("High values from January 2nd to August 25th")
<<<<<<< HEAD
plt.title("Date vs High Values from January 2nd to August 25th")
=======
plt.title("Date vs High Values from January 2nd to August 25")
>>>>>>> da75607e6ec85bd09a86987417a4abdc2386c36e

plt.show()
