import xmlrpc.client


def main():
    HOST = 'localhost'
    PORT = 8069
    DB = 'rd-demo'
    USER = 'manager'
    PASS = 'manager'

    root = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

    uid = xmlrpc.client.ServerProxy(root + 'common').login(DB, USER, PASS)

    sock = xmlrpc.client.ServerProxy(root + '2/object')
    args = [{
        'name': 'Session test xmlrpc',
        'start_date': '2022-01-27 10:30:00',
        'duration': 3.0,
        'number_of_seats': 10,
        'course_id': 2,
        'active': 'TRUE',
        }]
    sock.execute_kw(DB, uid, PASS, 'session', 'create', args)

    ids = sock.execute_kw(DB, uid, PASS, 'session', 'search', [[[1, '=', 1]]])
    sessions = sock.execute_kw(
        DB, uid, PASS, 'session', 'read',
        [ids], {'fields': ['name', 'number_of_seats']}
    )
    for session in sessions:
        print(f'{session["name"]} \t\t seats: {session["number_of_seats"]}')

if __name__ == '__main__':
    main()
