def main(): ...


def convert(time):
    time = time.split(":")
    time = int(time)
    time[1] = time[1] / 60


if __name__ == "__main__":
    main()
