def get_percent(x, y):
    percent = round(x / y * 100)
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


while True:
    fraction = input("format x/y")
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0 or x > y:
            print("Invalid. Try again")
            continue
    except (ValueError, ZeroDivisionError):
        raise ValueError
    percent = get_percent(x, y)
    print(percent)
    break
