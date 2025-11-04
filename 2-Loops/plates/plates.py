def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(vanity):
    zero_or_not = []
    if 6 >= len(vanity) >= 2:
        if vanity[0].isalpha() and vanity[1].isupper():
            if vanity[-1].isnumeric():
                for i in vanity:
                    # print(i)
                    if i.isalpha() or i.isnumeric():
                        # print(i)
                        if i.isnumeric():
                            zero_or_not.append(i)
                            # print(zero_or_not)
                            continue
                    else:
                        return False
    if len(zero_or_not) > 0:
        if zero_or_not[0] != "0":
            return True
    else:
        return False


main()
