import requests

LINK_AUTHORISATION = 'https://alexlisecky.amocrm.ru/oauth2/access_token'
CLIENT_ID = '61a68ebd-2c7f-4a18-83f3-a327675d56d7'
CLIENT_SECRET = '9IiWTRXsu5xnJ5IKoeToc7SA6nS5ZsaWu8oPLYpnhpMR7IGuN11CRLcBv6kdydN0'
REDIRECT_URI = 'https://example.com'


def get_access_token_with_authorization():
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': 'def50200e05cad5596a90aa3d204b8d134e94a299e766d52267370d84ea5c59b6958dc7ecca1774f9985c3b8b853fdbba1cf92ba1d9fe8e1fb07954a41e5a99b54159954e8d332c5f9d90f04b5954cafbf3f362d1cc8ce349bee67b9d3c7c0122fd9e9134c1071626e94e474c2856071890bc1c3d63f4e485fca034736d50a3d85f301e5071703c6c844f830037a74e66717ec4cc13be3def9dec3f07868972fca4ec115abfeaa77d8ca1aa6aa326adc5a480ed1caa79dc32bf04dc627b94abcd6488beac3ee08e30a99526fd97094574b09acfd5896a68735d240b78cc5511612142a5f35ba6d999daded706125b4af8dfb4b2f6940d2f68e4d4174407f5b0fb7eb292509e868aa0043ec7d78953f0a29909c026f34074de8697dcd0edfadbb1df6d2dc9ebe729566f49a6f7298d03b7e1081c18b603098e2979409e664a17e614f688ecfa079969529eb091d941b3fe7ddc5c57c4026791d1171dabbff198389cd186e24703b9357a7a607e8f3f426a79920cf01516e7075621515bd1c84104fea4bb047c626d6dd478bf2bf04eb035b429d733f1405631f09f96c6f1518a0b93bdad17f9818da70a10a71b38012761db7903323ace4a211c96b4624',
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(LINK_AUTHORISATION, data=data).json()

    return response


# response = get_access_token_with_authorization()
# print(response)

def get_access_token_on_refresh():
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": "def50200afebcfa6aec96cfc6858c8e0fc0b5dad4f1bf1b0293fda5da71911ccc950155ca340b8771fe955ae2161d2b33c6ed3cea1a6ee40d910410ac50001a857274fc03ef665d673e898443bb9217d01908455203e9cb6688b57704a2ba837d9e756a061157017948da68ecde55964adf26e42d2560becb0c074288ad7dd5080d4416b29e982e05ebcb89a619f228b4402eb314d17e57cde4e538d6f44fcf971c4fd656cbd2d3a0c0c573ad9e19c1e34c18ec9f8ae0d5f6067f7c85ebad948d1c4743ba82a2ace5f85367005ba22280ba14429e3143ba7e58526e4f568ac750281c12365fb53389918d884584d61b3cdd78a40c14faf43988c6cd773b97617907d3c40a34a203dc36cc60635b613cf2667714a285b43244bf229ac7a89f123d07d99d88ea9eacf2b6b2fbe96c218559408c9656bc34e5a1e58afc702b552ef6ef6175d97b77f14c72585dd1cc980ef7c5aedd78489361f152320f494c38dedd7559a11c617d490ef4d0120b6b21cdb8c6707a62a1ae15888c41a58f5d77e492611c03a92306d07d634d5e196064225c03134ea408c4bf1392424698ec2f1c836661810924de9400ce012b63522b2a52dd5e0d4daea726188dc84f65628753b7042d430621962a50885",
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(LINK_AUTHORISATION, data=data).json()

    return response


response = get_access_token_on_refresh()
print(response['access_token'])

access_token = response['access_token']


def get_deals():
    url = 'https://alexlisecky.amocrm.ru/api/v4/leads'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers).json()

    return response


def add_deals():
    url = 'https://alexlisecky.amocrm.ru/api/v4/leads'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.post(url, headers=headers)
