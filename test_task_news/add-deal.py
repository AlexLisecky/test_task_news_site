import requests

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjNjNzBjZjdhMDI5OWU0NjE4Njk2NjRlNWY0NmQ1YmRjZDJjOWEyZjg0ZmQ3YWMwYTVmZDc4MjA5MTI1Zjk2OTJjMmEzYTNiZWU1YjM4MmJmIn0.eyJhdWQiOiI2MWE2OGViZC0yYzdmLTRhMTgtODNmMy1hMzI3Njc1ZDU2ZDciLCJqdGkiOiIzYzcwY2Y3YTAyOTllNDYxODY5NjY0ZTVmNDZkNWJkY2QyYzlhMmY4NGZkN2FjMGE1ZmQ3ODIwOTEyNWY5NjkyYzJhM2EzYmVlNWIzODJiZiIsImlhdCI6MTY0MzM3MjA4NiwibmJmIjoxNjQzMzcyMDg2LCJleHAiOjE2NDM0NTc2ODYsInN1YiI6Ijc4NjM1MjAiLCJhY2NvdW50X2lkIjoyOTk2OTUzMywic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.NF-RfkaNZUa2tqbq3_S_LPpVmRNg9l3o6GkOVlZLDvZ8iJO_g5iYZp_Hm82SOQxowWwV0Z7zpIheXCbVlBjatsFT3o14LA3ag7UCGcDvDlCWmCBnR27pi-0Wxyi14PYCJXPjZMGkxqXfiW9u9UkXMdrCGyUHrdzYIDMagQ5687DqRjCWg-eEXjgCHOzSAPlJaH73E_AxI75-dlZQQmkpvmhi6JOhdBjj8qYUsMTxrEbTKQMj81wYc39ro4KhAZ9coD4g7lQhDbGXmWFwIRB8o4OZMSU_rts9zXwce4eenpIaRTkODU4NF2Zkr-ZaREvPx_TV70A0Q62ywUdROI9jSw'
URL = 'https://alexlisecky.amocrm.ru/api/v4/leads'
HEADERS = {'Authorization': 'Bearer',
           'access_token': access_token}


def add_deal():
    response = requests.post(url=URL, headers=HEADERS)
    print(response)


add_deal()
