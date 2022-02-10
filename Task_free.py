text = input()

text = text.split()

for item in text:
    print(item)

print(len(text))


textProp = set(text)
for item in textProp:
    print(item)

