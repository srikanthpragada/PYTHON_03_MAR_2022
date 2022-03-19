# Keyword only params
def wish(*, msg="Hi", name="Guest"):
    print(msg, name)


wish(name='Bill', msg="Hello")
wish(name="Scott")
wish()
# wish("Scott", "Hello")
