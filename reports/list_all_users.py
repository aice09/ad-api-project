def run(conn):
    conn.search('dc=your,dc=domain,dc=com',
                '(objectClass=user)',
                attributes=['sAMAccountName', 'displayName', 'mail'])

    return conn.entries
