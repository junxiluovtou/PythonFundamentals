import sys


def is_valid(stripped):
    if stripped == "" or stripped == "\n":
        return False
    elif stripped[0] == "#":
        return False
    else:
        return True


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    file = sys.argv[1]
    if file[-3:] != ".py":
        sys.exit("not a .py file")
    try:
        with open(file, "r", encoding="utf-8") as file:
            count = 0
            for line in file:
                stripped = line.lstrip()
                if is_valid(stripped) is True:
                    count += 1
                else:
                    continue
            print(count)
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
