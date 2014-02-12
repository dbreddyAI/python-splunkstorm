#!/usr/bin/env python

import urllib
import base64
import requests
try:
    import simplejson as json
except ImportError as e:
    import json

input_url = 'https://api.splunkstorm.com/1/inputs/http?'
project_id = None
access_token = None

def log(
    event_json,
    sourcetype='syslog',
    host=None,
    source=None
):

    if not project_id:
        raise Exception('project_id is required')
    if not access_token:
        raise Exception('access_token is required')

    params = {
        'project': project_id,
        'sourcetype': sourcetype
    }
    if host:
        params['host'] = host
    if source:
        params['source'] = source

    url = input_url + urllib.urlencode(params)

    payload = json.dumps(event_json)

    authorization = 'Basic ' + base64.b64encode(':'+access_token)
    headers = {'Authorization': authorization}

    return requests.post(
        url,
        data=payload,
        headers=headers
    )