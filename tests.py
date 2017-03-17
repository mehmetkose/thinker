
# Rethinkdb Wrapper For Tornado Framework
# https://github.com/mehmetkose/thinker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

import time
from thinker import Thinker

database = {
    'db': 'test',
    'host': '127.0.0.1',
    'port': 28015,
    'tables': {
        'user': {
            'user_name': {'default': None, 'specs': []},
            'user_mail': {'default': None, 'specs': []},
            'add_date': {'default': int(time.time()), 'specs': ['noedit', 'index']},
            'update_date': {'default': int(time.time()), 'specs': ['noedit', 'index']},
        }
    }
}
