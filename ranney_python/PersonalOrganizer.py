# defining functions
def addevent():
    # promoting user to enter value
    name = input("What is the event: ")
    month = int(input("What is the month (number): "))
    day = int(input("What is the date: "))
    year = int(input("What is the year: "))
    # validating date and month
    month = validatemonth(month)
    day = validateday(day,month,year)
    # appending into main
    eventMonth.append(month)
    eventDay.append(day)
    eventYear.append(year)
    eventName.append(name)


def validatemonth(a):
    # check if month is between 1 and 12
    if (a >= 1) and (a <= 12):
        return a
    else:
        return 1


def validateday(d, m, y):
    # validate date
    long_month = [1, 3, 5, 7, 8, 10, 12]
    short_month = [4, 6, 9, 11]
    # all long month have 31 days
    if (m in long_month) and (d >= 1) and (d <= 31):
        return d
    # all short month have 30 days
    elif (m in short_month) and (d >= 1) and (d <= 30):
        return d
    elif m == 2:
        # a gap year
        if (y % 4 == 0) and (y % 100 != 0):
            if (d >= 1) and (d <= 29):
                return d
            else:
                return 1
        # another gap year
        elif (y % 4 == 0) and (y % 100 == 0) and (y % 400 == 0):
            if (d >= 1) and (d <= 29):
                return d
            else:
                return 1
        # not a gap year
        elif y % 4 != 0:
            if (d >= 1) and (d <= 28):
                return d
            else:
                return 1
        else:
            return 1
    else:
        return 1


def printEvent():
    # convert month into word
    monthWord = ["NULL","January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    print("\n******************** List of Events ********************")
    for n in range(len(eventName)):
        # print event name
        print(eventName[n])
        # r int out date
        print("Date: " + str(monthWord[eventMonth[n]]) + ", " + str(eventDay[n]) + " " + str(eventYear[n]))

# main
# building array
eventName = []
eventMonth = []
eventDay = []
eventYear = []

# add 1st event
addevent()

# keep on adding event until stop
while input("Do you want to add another event? NO to stop: ") != "NO":
    addevent()

# print events
printEvent()
