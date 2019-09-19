import uuid as uuid_library
import hmac
import json
import hashlib
import requests
import six.moves.urllib as urllib




class instagram_api:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.LOGIN_URL = 'https://i.instagram.com/api/v1/accounts/login/'
        self.LOGOUT_URL = 'https://i.instagram.com/api/v1/accounts/logout/'
        self.like = 'https://i.instagram.com/api/v1/feed/liked'
        self.news = 'https://i.instagram.com/api/v1/news'
        self.timeline = 'https://i.instagram.com/api/v1/feed/timeline'
        self.popular = 'https://i.instagram.com/api/v1/feed/popular'
        self.DEVICE = {
        'instagram_version': '26.0.0.10.86',
        'android_version': 24,
        'android_release': '7.0',
        'dpi': '640dpi',
        'resolution': '1440x2560',
        'manufacturer': 'HUAWEI',
        'device': 'LON-L29',
        'model': 'HWLON',
        'cpu': 'hi3660'}
        self.REQUEST_HEADERS= { 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8' }
        self.IG_SIG_KEY = '99e16edcca71d7c1f3fd74d447f6281bd5253a623000a55ed0b60014467a53b1'
        self.USER_AGENT_BASE = (
            'Instagram {instagram_version} '
            'Android ({android_version}/{android_release}; '
            '{dpi}; {resolution}; {manufacturer}; '
            '{device}; {model}; {cpu}; en_US)'
        )

        self.user_agent = self.USER_AGENT_BASE.format(**self.DEVICE)

    def hex_digest(self, *args):
        m = hashlib.md5()
        m.update(b''.join([arg.encode('utf-8') for arg in args]))
        return m.hexdigest()

    def generate_device_id(self, seed):
        volatile_seed = "12345"  # Important ! :) :)
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def generate_uuid(self):
        return str(uuid_library.uuid4())

    def generate_signature(self,data):
        body = hmac.new(self.IG_SIG_KEY.encode('utf-8'), data.encode('utf-8'),hashlib.sha256).hexdigest() + '.' + urllib.parse.quote(data)
        signature = 'ig_sig_key_version=4&signed_body={body}'
        return signature.format(body=body)
    def time_for_action(self):
        phone_id = generate_uuid()
        uuid = generate_uuid()
        device_id = generate_device_id(hex_digest(USERNAME, USERNAME))

        data = json.dumps({
            'phone_id': phone_id,
            'device_id': device_id,
            'guid': uuid,
            'username': USERNAME,
            'password': PASSWORD,
        })

        data = generate_signature(data)

        session = requests.Session()
        session.headers.update(REQUEST_HEADERS)
        session.headers.update({'User-Agent': user_agent})
        response = session.post(LOGIN_URL, data=data)
        # print(response.content)
        response = session.post(like)
        jsoninverter = (json.loads(response.content))


USERNAME, PASSWORD = 'a.h.rahimi1993', 'mmae3477aMir!((#'

LOGIN_URL = 'https://i.instagram.com/api/v1/accounts/login/'
logoutURL = 'https://i.instagram.com/api/v1/accounts/logout/'
like = 'https://i.instagram.com/api/v1/feed/liked'
REQUEST_HEADERS = { 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8' }
IG_SIG_KEY = '99e16edcca71d7c1f3fd74d447f6281bd5253a623000a55ed0b60014467a53b1'

# I have more devices here:
# https://github.com/instagrambot/instabot/blob/72d10447986db39ac95f3d0980936d9c08428b02/instabot/api/devices.py
# idk which to use, let's for now use this one, because it is just works

DEVICE = {
    'instagram_version': '26.0.0.10.86',
    'android_version': 24,
    'android_release': '7.0',
    'dpi': '640dpi',
    'resolution': '1440x2560',
    'manufacturer': 'HUAWEI',
    'device': 'LON-L29',
    'model': 'HWLON',
    'cpu': 'hi3660'
}

USER_AGENT_BASE = (
    'Instagram {instagram_version} '
    'Android ({android_version}/{android_release}; '
    '{dpi}; {resolution}; {manufacturer}; '
    '{device}; {model}; {cpu}; en_US)'
)

user_agent = USER_AGENT_BASE.format(**DEVICE)  # just insert params
print(user_agent)


def hex_digest(*args):
    m = hashlib.md5()
    m.update(b''.join([arg.encode('utf-8') for arg in args]))
    return m.hexdigest()

def generate_device_id(seed):
    volatile_seed = "12345"  # Important ! :) :)
    m = hashlib.md5()
    m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
    return 'android-' + m.hexdigest()[:16]

def generate_uuid():
    return str(uuid_library.uuid4())

def generate_signature(data):
    body = hmac.new(IG_SIG_KEY.encode('utf-8'), data.encode('utf-8'),
                    hashlib.sha256).hexdigest() + '.' + urllib.parse.quote(data)
    signature = 'ig_sig_key_version=4&signed_body={body}'
    return signature.format(body=body)
phone_id = generate_uuid()
uuid = generate_uuid()
device_id = generate_device_id(hex_digest(USERNAME, USERNAME))

data = json.dumps({
    'phone_id': phone_id,
    'device_id': device_id,
    'guid': uuid,
    'username': USERNAME,
    'password': PASSWORD,
})

data = generate_signature(data)

session = requests.Session()
session.headers.update(REQUEST_HEADERS)
session.headers.update({'User-Agent': user_agent})
response = session.post(LOGIN_URL, data=data)
#print(response.content)
response = session.post(like)
jsoninverter = (json.loads(response.content))
jsoninverter = jsoninverter['items']

#spiltor = s.split('}')
#my_json = json.loads(s)
text_box = open('dictionary.txt', 'w+')
pruning = ['text','username','url']

def recursive():
    global jsoninverter
    global pruning
    global text_box
    printer= []

    for i in range(len(jsoninverter)):
        indexer = {}
        indexer['index'] = i
        indexer['like_count'] = jsoninverter[i]['like_count']
        indexer['id']=jsoninverter[i]['pk']

        indexer['profile_pic']= jsoninverter[i]['user']['profile_pic_url']
        indexer['username'] =  jsoninverter[i]['user']['username']
        indexer['fullname'] = jsoninverter[i]['user']['full_name']

        image_pathes = []
        try:
            for j in range(len(jsoninverter[i]['carousel_media'])):
                image_pathes.append(jsoninverter[i]['carousel_media'][j]['image_versions2']['candidates'][0]['url'])
        except:
            image_pathes.append(jsoninverter[i]['image_versions2']['candidates'][0]['url'])
        indexer['share_post'] = image_pathes
        comment=[]
        try:
            for j in range(len(jsoninverter[i]['preview_comments'])):
                comment.append((jsoninverter[i]['preview_comments'][j]['text'] , jsoninverter[i]['preview_comments'][j]['user']['username'] , jsoninverter[i]['preview_comments'][j]['user']['profile_pic_url'] , jsoninverter[i]['preview_comments'][j]['user']['is_private']))
            indexer['comments']= comment
        except:
            try:
                if jsoninverter[i]['comments_disabled']== True:
                    indexer['comments']= 'comments_disabled'
            except:
                indexer['comments'] = 'None'
        try:
            indexer['caption'] = jsoninverter[i]['caption']['text']
        except:
            indexer['caption']= 'None'
        try:
            indexer['location']= (jsoninverter[i]['location']['name'] , jsoninverter[i]['location']['adress'] , jsoninverter[i]['location']['short_name'], jsoninverter[i]['location']['lang'], jsoninverter[i]['location']['lat']
        except:
            indexer['location']='None'
        try:
            indexer['user_tag']=jsoninverter[i]['usertags']
        except:
            indexer['user_tag']='None'

        printer.append(indexer)

recursive()
response= session.post(logoutURL)
assert response.status_code == 200
