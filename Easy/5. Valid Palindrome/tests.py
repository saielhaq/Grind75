s = "race a car"
clean = ''
for char in s.lower():
    if char.isalnum():
        clean += char
rev = clean[::-1]
print(rev == clean)

