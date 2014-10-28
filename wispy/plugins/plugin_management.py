import wispy
import wispy.core

def list_plugins(reply, user, typeargs, args, conn, event):
    reply(", ".join(conn.plugins))

def unload_plugin(reply, user, typeargs, args, conn, event):
    if typeargs[0] not in conn.plugins:
        return reply("Error: %s is not loaded." % typeargs[0])
    conn.unregister_callbacks(typeargs[0])
    conn.plugins.remove(typeargs[0])
    reply("%s unloaded." % typeargs[0])

def load_plugin(reply, user, typeargs, args, conn, event):
    try:
        wispy.core.load_plugin(conn, typeargs[0])
        reply("%s loaded." % typeargs[0])
    except:
        reply("%s failed to load!" % typeargs[0])

def register_callbacks(conn):
    conn.register_command("plugins", list_plugins, send_extra_info=True)
    conn.register_command("load", load_plugin, str, send_extra_info=True, permission="admin")
    conn.register_command("unload", unload_plugin, str, send_extra_info=True, permission="admin")
