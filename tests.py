
# Rethinkdb wrapper for asyncio
# https://github.com/mehmetkose/thinker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

import time
import unittest
import asyncio
import inspect

from thinker import Thinker

scheme = {
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

def async_test(f):
    def wrapper(*args, **kwargs):
        if inspect.iscoroutinefunction(f):
            future = f(*args, **kwargs)
        else:
            coroutine = asyncio.coroutine(f)
            future = coroutine(*args, **kwargs)
        asyncio.get_event_loop().run_until_complete(future)
    return wrapper

class ThinkerTest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @async_test
    async def test_tcp3_fail(self):
        db = await Thinker.init(scheme=scheme, create_scheme=True)
        user_list = await db.all("user")
        self.assertListEqual([], user_list)

if __name__ == "__main__":
    unittest.main()
