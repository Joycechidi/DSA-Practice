#Calculate average temperature

numDays = int(input("How many days temperature? "))

total = 0
temp = []
for i in range(1, numDays+1):
    nextDay = int(input("Day " + str(i+1) + "'s high temperature is : "))
    temp.append(nextDay)
    total += temp[i]

avg = round(total/numDays, 2)
print("\nAverage = " + str(avg))

#Find the number of days above average temperature
above = 0
for i in temp:
    if i > avg:
        above += 1
print(str(above) + " days above average temperature")
