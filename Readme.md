

Install
---

    $ pip install splunkstorm

Use
---

```python

import splunk
splunk.project_id = ''
splunk.access_token = ''

splunk.log({
  'event': 'event',
  'duration': '5ms'
})

```