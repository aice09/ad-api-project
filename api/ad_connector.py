from ldap3 import Server, Connection, ALL
import json

def connect():
    with open('config/settings.json') as f:
        config = json.load(f)

    server = Server(config["domain_controller"], get_info=ALL)
    conn = Connection(server, user=config["username"], password=config["password"], auto_bind=True)
    return conn
