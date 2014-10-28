from pyirc import irc
from functools import wraps
import wispy.plugins
import importlib

class ConnectionWrapper:
    """
    A per-plugin wrapper for pyirc.irc.IRCConnection.
    Provides:
    - An overridden register_callback which sets callback tags
    - The register_command function

    It's worth noting that this is **not** a subclass of IRCConnection, rather,
    it achieves similar functionality by defining __getattr__.
    """
    def __init__(self, conn, pluginname):
        self.conn = conn
        self.bot = conn
        self.pluginname = pluginname

    def __getattr__(self, attr):
        if thing not in self.__dict__:
            return conn.__dict__.get(attr, None)
        return self.__dict__[attr]

    def register_callback(self, type, func):
        self.conn.register_callback(type, func, self.pluginname)

    def register_command(self, command, callback, *argtypes, **options):
        command_options = {"send_extra_info": False, "permission": None}
        command_options.update(options)
        @wraps(callback)
        def command_handler(conn, event):
            if command_options["permission"] is not None:
                if event.user.host not in self.conn.config["permissions"][command_options["permission"]]:
                    return
            if event.etype == "pubmessage":
                if not event.message.startswith(conn.config["misc"]["command_trigger"]):
                    return
                msg = event.message[len(conn.config["misc"]["command_trigger"]):]
                reply_to = lambda m: conn.say(event.to, m)
            else:
                msg = event.message
                reply_to = lambda m: conn.say(event.user.nick, m)
            args = msg.split()
            if args[0] != command:
                return
            args = args[1:]
            try:
                typeargs = [argtype(args[n]) for n, argtype in enumerate(argtypes)]
            except IndexError:
                reply_to("Invalid argument signature. Should be %s" % repr(argtypes))
                return
            if command_options["send_extra_info"]:
                callback(reply_to, event.user, typeargs, args, conn, event)
            else:
                callback(reply_to, event.user, *typeargs)
        self.register_callback("pubmessage", command_handler)
        self.register_callback("privmessage", command_handler)

def load_plugin(conn, plugin):
    importlib.invalidate_caches()
    module = importlib.import_module('.%s' % plugin, 'wispy.plugins')
    module.register_callbacks(ConnectionWrapper(conn, plugin))
    conn.plugins.append(plugin)

def start(config):
    """
    The main bot entry point.
    """
    host = config["server"]["host"]
    port = config["server"]["port"]
    nick = config["identity"]["nickname"]
    ident = config["identity"]["ident"]
    realname = config["identity"]["realname"]
    password = config["identity"]["password"]
    channels = config["channels"]

    conn = irc.do_irc_connect(host, port)
    conn.register(nick, ident, realname, password)
    conn.autojoin(*channels)
    conn.config = config
    conn.plugins = []

    for plugin in config["plugins"]:
        load_plugin(conn, plugin)
