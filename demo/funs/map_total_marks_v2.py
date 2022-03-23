st = "84,45,65,ab,45,34,90"

nums = filter(str.isdigit, st.split(","))
total = sum(map(int, nums))

print(total)
