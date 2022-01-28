import json

import requests

LINK_AUTHORISATION = 'https://alexlisecky.amocrm.ru/oauth2/access_token'
CLIENT_ID = '61a68ebd-2c7f-4a18-83f3-a327675d56d7'
CLIENT_SECRET = '9IiWTRXsu5xnJ5IKoeToc7SA6nS5ZsaWu8oPLYpnhpMR7IGuN11CRLcBv6kdydN0'
REDIRECT_URI = 'https://example.com'


# def get_access_token_with_authorization():
#     data = {
#         'client_id': CLIENT_ID,
#         'client_secret': CLIENT_SECRET,
#         'grant_type': 'authorization_code',
#         'code': 'def502006f9e054da5c8fe3832421830b96efb7f9095159e0762c2b5184ebe2aa670c5b5e65652e27b4c33c2c71eb1e94380acdeaec3f6cb8a5b49f701ade3788c3ea1daa476a7372798dded002c80cc91a4220f4f7afb94beb3ebc3e67481542340ef9919b4f2aa07b8e305acedbf25e4de543bd7bf3ed2060aa4d5c4ded46cdb6137d87ac920927bec85106fc93b4e880f498ba3d16c33958bb2edf883f131c1902a6dcb2246964cfeae208d9e866c4a719dd584c2cd2f9e3fe69a3321487c2cedda247e664a94f47959a203afe8368bc6e88924c12b4316a7723343ef6f2975ee98a255578970a904f334bc5a9ffd60a37721f4edac15c5cc9795d73654729f9ef00992311e02e162acc2f4e3875448793c0baa5c6ba36a97643f0cdf6c250a0eca6d47e0c8b06e11e063af895735880cb2f95dc5399fa0f3055899502e59ff87dd0125bb8e4e7b61e212cb0647b3d96ab3f8aaa856c8da5af5fd7b89385df01beef6994d64993459cedabc3d37c0fc0476a85cb8d19bbbb9fe2da319885a1dc1316f49a28e41ec7f59dc0df0e743e58a28d656f3f8cfaf0d59a8f30ea9692a01006e3e8f089edecb46dc325c6fed22e1ef1ac43cf328c1999211ec',
#         'redirect_uri': REDIRECT_URI
#     }
#
#     response = requests.post(LINK_AUTHORISATION, data=data).json()
#
#     return response
#
#
# response = get_access_token_with_authorization()
# print(response['refresh_token'])

#

def get_access_token_on_refresh():
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": 'def50200df032c126b60ec517e9bae804b0c131087ae8912269bd2595ca451f06d56414afbf973273c9de66f34150332bfdf37c6892b944bf8b7a7817155506d54c19d222765a0c4dda5dd6f384a34003c9db036e0c7361574436d6c9fa78b43059af9f0ac5d27df8029f8d85c0262b3f75fe83f3c7e2de07a8ad066d34a1b3261378022dc6bba4d301b8d2f97623cf7132adf5a412a80a4576ac9ce27fcd63df3199d5938ed768e89b8fdd01d6f80a9b1688514af632f93d62072c047fb7aaa585f6cbba2bb9c60ac61e37db5348019d1ae0c49fafb5ba976b6cde90f2a51819db6136dcf39af826869e07d1c762b64082ee77ff928d28437fa0fbb7f03868620597b1c64d5603de416030bc5a1cce9311416fa48b196cb8bbceca1043ea4110da3708863fbe79dd7cb2db94076fe6d58fd504611da23318f479c6ec156ffa82ea919619d1c167a470765eacf1ebed04e901fd6c4eca6394a456e02e78e33c230d351034e8faefa03c33bb8a88e9a8bcc49f7770ccba6e4468a9079b93e7f0fa039214cc3263c398c84c05210f40f0c78bc5b68fe4296ed05fa17f8e28c7bf2338318d203751e3d46e7f2ba165de440feb42731437426e69da6f0cc68e8dbba896ff93563d0146a1e8f',
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(LINK_AUTHORISATION, data=data).json()

    return response


response = get_access_token_on_refresh()
print(response)
access_token = response['access_token']


def get_deals():
    url = 'https://alexlisecky.amocrm.ru/api/v4/leads'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers).json()

    return response


def add_deals():
    url = 'https://alexlisecky.amocrm.ru/api/v4/leads/complex'
    headers = {'Authorization': 'Bearer ' + access_token}
    data = [{
        'name': 'test',
        'price': 5000,
        '_embedded': {
            'contacts': [
                {
                    'first_name': 'alex',

                }
            ]
        }
    }
    ]
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())


add_deals()
