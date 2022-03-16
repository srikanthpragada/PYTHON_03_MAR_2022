
st = "how do you do today?"

for c in sorted(set(st)):
    print(f"{c} - {st.count(c)}")

