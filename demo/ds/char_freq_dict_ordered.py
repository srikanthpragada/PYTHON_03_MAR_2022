# Char freq in the order of chars
st = "how do you do today?"

chars = {}
for c in st:
    count = chars.get(c, 0)
    chars[c] = count + 1

print(chars)

