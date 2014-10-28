def eval_from_irc(reply, user, typeargs, args, conn, event):
    reply(eval(event.message.split(" ", maxsplit=1)[1]))

def exec_from_irc(reply, user, typeargs, args, conn, event):
    exec(event.message.split(" ", maxsplit=1)[1])

def register_callbacks(conn):
    conn.register_command("eval", eval_from_irc, str, send_extra_info=True, permission="admin")
    conn.register_command("exec", exec_from_irc, str, send_extra_info=True, permission="admin")
