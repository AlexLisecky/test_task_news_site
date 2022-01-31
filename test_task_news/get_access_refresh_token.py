import json
import requests

LINK_AUTHORISATION = 'https://alexlisecky.amocrm.ru/oauth2/access_token'
CLIENT_ID = '61a68ebd-2c7f-4a18-83f3-a327675d56d7'
CLIENT_SECRET = '9IiWTRXsu5xnJ5IKoeToc7SA6nS5ZsaWu8oPLYpnhpMR7IGuN11CRLcBv6kdydN0'
REDIRECT_URI = 'https://example.com'


def get_access_token():
    """
    Получение access_token из json-файла
    :return str access_token
    """

    with open('token_amo.json', 'r', encoding='utf-8') as file:
        file_content = json.load(file)
        access_token = file_content['access_token']

    return access_token


# def get_access_token_with_authorization():
#     data = {
#         'client_id': CLIENT_ID,
#         'client_secret': CLIENT_SECRET,
#         'grant_type': 'authorization_code',
#         'code': 'def50200c3934ad1140f36490ab025bd09d0ed31cf82c2b2647e4464533ed0625d6e0ac5ef3a8d5921bac6e95c27d76169f011e487c820f6cd06c1cc4ed96bd7f1f2231def36f5eed666c174acba412a26d7bac69fcef54f879f65a2bdc073d7982d4b5e19bfcc250a8f92cc6d59dc6198e3bf50854170f705ce4c078e0aa784fc98ed0e029b75f804a0d3fe91c430743b6b5ff29533bb3751f84a7bdde021a897ebe94ff9e680b3ce245466775b8ec935b261d9bed8f2a1ef51465ddf226495b9241dbc4091125950bce2f7c7c800ed25add10eaa699c53b76018043bea9f19572dc5fbeb05890b788ddb1dbd17edf656bc4c30382c441d4f7d10b6690bd6351c4199f0fb061973e5a740095b7d6a4353526e4ef869189b931f3db52c4ef2cb6d178896b94b1fba5cd1ea61ed647da6073865f54b4aad134bc15e6fd5621c20b2453edf83c590376f8bbdc9a9a087729d594e17a7678fc57f0924d0a21903e8b97fc92c538c1385a55f8a95f8af6ba11ed70eb473a3a00ca633dad40f3fcd56ff0859bda250c2b3d5ddccb26a74efcc42f4d565a709918a58413df404fcbadd2dfbc63ce0c5237c79f35d300826d4ba1c209a44868aee0f96b4b461f2',
#         'redirect_uri': REDIRECT_URI
#     }
#
#     response = requests.post(LINK_AUTHORISATION, data=data).json()
#
#     with open('token_amo.json', 'w', encoding='utf-8') as file:
#         json.dump(response, file, indent=4, ensure_ascii=False)
#
#     return response
#
#
# response = get_access_token_with_authorization()
# print(response)


# def get_access_token_on_refresh():
#     with open('token_amo.json', 'r', encoding='utf-8') as file:
#         file_content = json.load(file)
#         refresh_token = file_content['refresh_token']
#
#     data = {
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#         "grant_type": "refresh_token",
#         "refresh_token": refresh_token,
#         "redirect_uri": REDIRECT_URI
#     }
#
#     response = requests.post(LINK_AUTHORISATION, data=data).json()
#
#     with open('token_amo.json', 'w', encoding='utf-8') as file:
#         json.dump(response, file, indent=4, ensure_ascii=False)
#
#     return response
#
#
# response = get_access_token_on_refresh()
# print(response)
#
#
def get_deals():
    access_token = get_access_token()

    url = 'https://alexlisecky.amocrm.ru/api/v4/leads'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers).json()

    return response


def add_deals():
    access_token = get_access_token()

    url = 'https://alexlisecky.amocrm.ru/api/v4/leads/complex'
    headers = {'Authorization': 'Bearer ' + access_token}
    data = [
        {
            'name': 'test',
            'price': 11000,
            '_embedded': {
                'contacts': [
                    {
                        'first_name': 'alex',
                        'last_name': 'lisecky',
                        'created_at': 1643580468,
                    }
                ],
                'companies': [
                    {
                        'name': 'test_company',
                        'custom_fields_values': [
                            {
                                'field_code': 'PHONE',
                                'values': [
                                    {
                                        "value": "+7912322222",
                                        "enum_code": "WORK"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "custom_fields_values": [
                    {
                        "field_id": 5,
                        "values": [
                            {
                                "value": True
                            }
                        ]
                    }
                ],
            }
        }
    ]
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
    print('успешно')


add_deals()
