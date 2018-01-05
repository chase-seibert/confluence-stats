from functools import partial
import time
from pyfluence import Confluence


_CREDENTIALS_FILE = '.credentials'


def login_from_credentials():
    with open(_CREDENTIALS_FILE, 'r') as fd:
        username = fd.readline().strip()
        password = fd.readline().strip()
        base_url = fd.readline().strip()
    api = Confluence(username, password, base_url)
    return api


if __name__ == '__main__':
    print 'Example API root: https://mycompany.atlassian.net/wiki)'
    base_url = raw_input('Confluence API root: ')
    username = raw_input('Confluence username: ')
    password = raw_input('Confluence password: ')
    try:
        api = Confluence(username, password, base_url)
        # TODO: some test here
    except Exception as e:
        print e.response.text
        exit(1)
    print 'Success, writing credentials to %s' % (_CREDENTIALS_FILE)
    with open(_CREDENTIALS_FILE, 'w') as fd:
        fd.write(username + '\n')
        fd.write(password + '\n')
        fd.write(base_url + '\n')
