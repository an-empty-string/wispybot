import ast
def set_config(reply, user, typeargs, args, conn, event):
    key = typeargs[0].split(".")
    val = typeargs[1]
    conf = conn.config
    try:
        for i in key[:-1]:
            conf = conf[i]
        conf[key[-1]] = ast.literal_eval(val)
    except KeyError:
        reply("Failure!")
    reply("Success!")

def get_config(reply, user, typeargs, args, conn, event):
    key = typeargs[0].split(".")
    conf = conn.config
    try:
        for i in key[:-1]:
            conf = conf[i]
        reply(conf[key[-1]])
    except:
        reply("Nonexistent configuration key")

def register_callbacks(conn):
    conn.register_command("config set", set_config, str, str, send_extra_info=True, permission="admin")
    conn.register_command("config get", get_config, str, send_extra_info=True, permission="admin")
