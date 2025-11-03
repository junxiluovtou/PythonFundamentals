camel = input()
snake = ""
for i in camel:
    if i.islower():
        snake = snake + i
    elif i.isupper():
        snake = snake + "_" + i.lower()
print(snake)
