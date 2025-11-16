months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    date = input()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            if int(month) < 10:
                month = "0" + month
                print(month)
            if int(day) < 10:
                day = "0" + day
                print(day)
            print(f"{year}/{month}/{day}")

        else:
            date = date.replace(",", "")
            # print(date)
            month, day, year = date.split()
            print(month, year)
            if month in months:
                month = months.index(month) + 1
                if month < 10:
                    month = "0" + str(month)
                print(month)
                if int(day) < 10:
                    day = "0" + day
            print(f"{year}/{month}/{day}")
    except:
        date = input()
