# Calculate net price with a discount of 15%

data = input("Enter price : ")
price = int(data)  # convert str to int
discount = price * 15 / 100
net_price = price - discount
print("Net price = ", net_price)
