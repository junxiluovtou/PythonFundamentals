i = input()
if i == "42":
    print("Yes")
elif i.lower().replace("-", " ") == "forty two":
    print("Yes")
else:
    print("No")
