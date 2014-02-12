#!/usr/bin/env python
import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lib as splunk

class TestCase(unittest.TestCase):

    def test_post(self):

        splunk.access_token = ''
        splunk.project_id = ''

        splunk.log({
          'event': 'event',
          'duration': '5ms'
        })

        # TODO: more test

unittest.main()