from matplotlib.pyplot import plot, bar, show

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


bar = bar(year, bestAvg)
chart = plot(year, battingAvg)
show()