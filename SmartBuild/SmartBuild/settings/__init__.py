from _enviroments import get_server_type
exec("from %s import *" % get_server_type())
