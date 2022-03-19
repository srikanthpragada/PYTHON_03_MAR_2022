# positional only params
def wish(message="Hi", name="Guest", /):
    print(message, name)


wish("Hello", "Steve")
wish("Hi")
wish(name="Tom")
