#Testing making a graph for Amazon yearly revenue
import pandas
import matplotlib.pyplot as plt

AMZN = "Amazondata.csv"
Amazon = pandas.read_csv(AMZN)
print(Amazon)

Year = Amazon.Year
Revenue = Amazon.Revenue

plt.plot(Year,Revenue)

plt.xlabel("Year")
plt.ylabel("Revenue")
plt.title("Yearly Revenue for Amazon")

plt.show()