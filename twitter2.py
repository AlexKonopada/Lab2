import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import twurl


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def data_from_twitter2():
    acct = input('Enter Twitter Account:')
    # if len(acct) < 1:
    #     break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})
    # print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    return js
        # print(js)
        # print(json.dumps(js, indent=2))
    # headers = dict(connection.getheaders())
    # print('Remaining', headers['x-rate-limit-remaining'])

    # for user in js['users']:
    #     print(user['screen_name'])
    #     if 'status' not in user:
    #         print('   * No status found')
    #         continue
    #     status = user['status']['text']
    #     print('  ', status[:50])
