# Calculate net price with a discount of 15%

data = input("Enter price : ")
price = int(data)  # convert str to int
discount = price * 15 / 100
net_price = price - discount

print(f"Price       {price:8.2f}")
print(f"-Discount   {discount:8.2f}")
print(f"            --------")
print(f"Net price   {net_price:8.2f}")
