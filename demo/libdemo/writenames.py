# Create names.txt and write names into it
with open("names.txt","wt") as f:
     while True:
         name = input("Enter name [end to stop] :")
         if name == "end":
             break

         f.write(name + "\n")

print("The End")