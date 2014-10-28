def join_channel(reply, user, typeargs, args, conn, event):
    conn.join(typeargs[0])
    reply("Joined %s." % typeargs[0])

def part_channel(reply, user, typeargs, args, conn, event):
    conn.part(typeargs[0])
    reply("Left %s." % typeargs[0])

def register_callbacks(conn):
    conn.register_command("join", join_channel, str, send_extra_info=True, permission="admin")
    conn.register_command("part", part_channel, str, send_extra_info=True, permission="admin")
