import ast
def get_config_key(conn, key, final=False):
    conf = conn.config
    try:
        for i in (key if final else key[:-1]):
            conf = conf[i]
    except:
        return {}
    return conf

def set_config(reply, user, typeargs, args, conn, event):
    key = typeargs[0].split(".")
    val = typeargs[1]
    try:
        conf = get_config_key(conn, key)
        conf[key[-1]] = ast.literal_eval(val)
        reply("Success!")
    except KeyError:
        reply("Failure!")

def add_config(reply, user, typeargs, args, conn, event):
    key = typeargs[0].split(".")
    val = typeargs[1]
    try:
        conf = get_config_key(conn, key)
        conf[key[-1]].append(ast.literal_eval(val))
        reply("Success!")
    except:
        try:
            conf[key[-1]].append(val)
            reply("Success!")
        except:
            reply("Failure!")

def get_config(reply, user, typeargs, args, conn, event):
    key = typeargs[0].split(".")
    try:
        conf = get_config_key(conn, key, True)
        reply(conf)
    except:
        reply("Nonexistent configuration key")

def register_callbacks(conn):
    conn.register_command("config set", set_config, str, str, send_extra_info=True, permission="admin")
    conn.register_command("config get", get_config, str, send_extra_info=True, permission="admin")
    conn.register_command("config add", add_config, str, str, send_extra_info=True, permission="admin")
