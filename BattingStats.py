#Crosby Ravert and Akshit Pathania
#Pitt-Bradford: Object Oriented Programming, Spring 21
from matplotlib.pyplot import plot, bar, show, subplots
import matplotlib.pyplot as plt

file = open("batting.csv")
file.readline()

year = []
battingAvg = []
bestAvg = []
tempYearAvgs = []
yearCounter = 1871
batterCount = 0
yearlyAvg = 0

for line in file:
    value = line.split(',')
    hits = int(value[8])
    atBat = int(value[6])
    statYear = int(value[1])
    if atBat != 0:
        if statYear == yearCounter:
            avg = (hits / atBat)
            tempYearAvgs.append(avg)
            yearlyAvg += avg
            batterCount += 1
        else:
            if batterCount != 0:
                realYearlyAvg = yearlyAvg / batterCount
                year.append(yearCounter)
                battingAvg.append(realYearlyAvg)
            bestAvg.append(max(tempYearAvgs))
            yearCounter += 1
            batterCount = 0
            yearlyAvg = 0
            tempYearAvgs.clear()
            avg = (hits / atBat)
            tempYearAvgs.append(avg)
            yearlyAvg += avg
            batterCount += 1
    else:
        continue


fig, (ax1, ax2) = subplots(2)
fig.suptitle("Average of yearly batting averages over the best average")
ax1.plot(year, battingAvg)
ax2.bar(year, bestAvg)
show()