def pre(c,e):
    print(e)

def register_callbacks(c):
    c.register_callback("irc", pre)
