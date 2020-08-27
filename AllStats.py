#Run this to see all companies' yearly revenue.
#All info comes from macrotrends.com
import pandas

AMZN = "Amazondata.csv"
Amazon = pandas.read_csv(AMZN)
print("")
print("Yearly revenue for Amazon:")
print(Amazon)

APPL = "Appledata.csv"
Apple = pandas.read_csv(APPL)
print("")
print("Yearly revenue for Apple:")
print(Apple)

FB = "Facebookdata.csv"
Facebook = pandas.read_csv(FB)
print("")
print("Yearly revenue for Facebook:")
print(Facebook)

NFLX = "Netflixdata.csv"
Netflix = pandas.read_csv(NFLX)
print("")
print("Yearly revenue for Netflix:")
print(Netflix)

MSFT = "Microsoftdata.csv"
Microsoft = pandas.read_csv(MSFT)
print("")
print("Yearly revenue for Microsoft:")
print(Microsoft)

