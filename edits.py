import argparse
from collections import Counter, defaultdict
import time
from login import login_from_credentials


_RESULTS_FILE = 'edits.csv'
stats = defaultdict(lambda: defaultdict(int)) # {'user1': {'created': 1, 'edited': 5}}


def generate_stats(start=None, space=None, sleep=None):
    api = login_from_credentials()
    data = api.search('type=page and lastModified>%s %s' % (
        start,
        (' and space=%s' % space) if space else ''
    ))

    print 'Found %s pages' % data['size']
    pages = data['results']
    for page in pages:
        print '%s %s' % (_day(page['lastModified']), page['title'])
        id = page['content']['id']
        content = api.get_content(id)  # TODO might be able to skip this
        stats[content['version']['by']['displayName']]['created'] += 1
        history = api._query('content/%s/version' % id)
        for version in history['results']:
            when = version['when']
            if when < start:
                break
            print '%s Version %s' % (_day(when), version['number'])
            stats[version['by']['displayName']]['edited'] += 1
            write_file()
        time.sleep(sleep)
    return stats


def _day(date):
    return date[:10]


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=str, help='Start date, format: 2017-01-01')
    parser.add_argument('--space', type=str, help='A single space to pull from')
    parser.add_argument('--sleep', type=int, default=0, help='Sleep time in seconds to avoid rate limiting')
    args = parser.parse_args()
    return args


def write_file():
    with open(_RESULTS_FILE, 'w') as fd:
        fd.write('username,created,edited\n')
        for username, counts in stats.items():
            fd.write('%s,%s,%s' % (username, counts['created'], counts['edited']))
            fd.write('\n')


def _get_pages(space=None):
    pass


def _get_edits(page):
    pass


if __name__ == '__main__':
    options = parse_options()
    stats = generate_stats(**options.__dict__)
    print 'Writing to %s' % _RESULTS_FILE
    write_file()
