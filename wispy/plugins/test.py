def hello_command(reply, user, hello_target):
    reply("Hello, %s!" % hello_target)

def register_callbacks(bot):
    bot.register_command("hello", hello_command, str)
