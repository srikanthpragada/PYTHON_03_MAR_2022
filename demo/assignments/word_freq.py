# Word Freq
st = "How do you do today How did you do yesterday"
words = st.split(" ")

for w in set(words):
    print(f"{w} - {words.count(w)}")


