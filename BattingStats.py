from matplotlib.pyplot import plot
import matplotlib

file = open("batting.csv")
file.readline()

year = []
battingAvg = []
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
            yearlyAvg += avg
            batterCount += 1
        else:
            if batterCount != 0:
                realYearlyAvg = yearlyAvg / batterCount
                year.append(yearCounter)
                battingAvg.append(realYearlyAvg)
            yearCounter += 1
            batterCount = 0
            yearlyAvg = 0
            avg = (hits / atBat)
            yearlyAvg += avg
            batterCount += 1
    else:
        continue


chart = plot(year, battingAvg)
matplotlib.pyplot.show()