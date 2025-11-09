i = input()


def valid(inp):
    username = "junxi"
    special_contained = False
    specialchars = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "+",
        "[",
        "]",
        ":",
        ";",
        '"',
        "'",
        "<",
        ",",
        ">",
        ".",
        "/",
        "?",
        "\\",
    ]
    # print(specialchars)
    upper_included = False
    lower_included = False
    acceptable = True
    while acceptable == True:
        if 20 >= len(inp) >= 6:
            acceptable = True
        else:
            print("less than 6 or over 20 chars")
            acceptable = False
        for i in inp:
            if i.isupper():
                upper_included = True
            elif i.islower():
                lower_included = True
            if i in specialchars:
                special_contained = True
        if upper_included == True and lower_included == True:
            acceptable = True
        else:
            print("Doesn't contain at least one uppercase and one lowercase letter")
            acceptable = False
        if specialchars == True:
            acceptable = True
        else:
            print("needs to Contain at least one of the following special character")
            acceptable = False
        if " " in inp:
            print("No spaces")
            acceptable = False
        if username in inp:
            print("can't contain username")
            acceptable = False
        if "password" or "1234" or "qwerty" in inp:
            print("can't have these")
            acceptable = False
    if acceptable == True:
        print("Valid")
    else:
        print("Invalid")


valid(i)
