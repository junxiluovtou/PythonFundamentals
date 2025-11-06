def main():
    i = input()
    convert(i)


def convert(time):
    time = time.split(":")
    # time = int(time)
    time[1] = int(time[1]) / 60
    # print(time[0] + time[1])
    t = int(time[0]) + time[1]
    if 8 >= t >= 7:
        print("breakfast")
    elif 13 >= t >= 12:
        print("lunch")
    elif 19 >= t >= 18:
        print("dinner")
    else:
        print("nothing")


if __name__ == "__main__":
    main()
