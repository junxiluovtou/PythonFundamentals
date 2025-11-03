word = input()
new_word = ""
vowels = ["A", "E", "I", "O", "U"]
for i in word:
    if i.upper() in vowels:
        continue
    else:
        new_word = new_word + i
print(new_word)
