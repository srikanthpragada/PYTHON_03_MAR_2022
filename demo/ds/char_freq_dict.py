
st = "how do you do today?"

chars = {}
for c in set(st):
    chars[c] = st.count(c)

print(chars)

