Generate stats on number of pages/edits/comments by user against your Confluence instance.

# Quickstart

To crawl your confluence instance, looking for all posts modified since
July, 2017, and tally up new pages, edits and comments by user in the space ENG:

```bash
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python login.py
python edits.py --space ENG --start 2017-07-01
```

Example output:

```bash
username,created,edited
User 1,0,2
User 2,0,22
User 3,0,4
User 4,0,5
```
