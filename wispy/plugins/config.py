import ast
def set_config(reply, user, typeargs, args, conn, event):
    key = typeargs[0].split(".")
    val = typeargs[1]
    conf = conn.config
    try:
        for i in key[:-1]:
            conf = config[i]
        conf[key[-1]] = ast.literal_eval(val)
    except KeyError:
        reply("Failure!")
    reply("Success!")

def register_callbacks(conn):
    conn.register_command("config_set", set_config, send_extra_info=True, permission="admin")
