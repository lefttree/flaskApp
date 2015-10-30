try:
    import httplib  # Python 2
except ImportError:
    import http.client as httplib  # Python 3
try:
    from urllib import urlencode  # Python 2
except ImportError:
    from urllib.parse import urlencode  # Python 3
import json
from flask.ext.babel import gettext
from config import MS_TRANSLATOR_CLIENT_ID, MS_TRANSLATOR_CLIENT_SECRET
import traceback

def microsoft_translate(text, sourceLang, destLang):
    if MS_TRANSLATOR_CLIENT_ID == "" or MS_TRANSLATOR_CLIENT_SECRET == "":
        return gettext('Error: translation service not configured.')
    try:
        # method 1
        # oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/oauth2-13'
        # # need to decode 'utf-8'
        # oauth_junk = json.loads(requests.post(oauth_url,data=urllib.parse.urlencode(params)).content.decode('utf-8'))
        # translation_args = {
        # 'text': "hello",
        # 'to': destLang,
        # 'from': sourceLang
        # }
        # headers={'authorization': 'bearer '+oauth_junk['access_token']}
        # translation_url = 'http://api.microsofttranslator.com/v2/ajax.svc/translate?'
        # translation_result = requests.get(translation_url+urllib.parse.urlencode(translation_args),headers=headers)
        # return translation_result.content

        # method 2
        # client = azure_translate_api.MicrosoftTranslatorClient(MS_TRANSLATOR_CLIENT_ID, MS_TRANSLATOR_CLIENT_SECRET)     
        # return client.TranslateText('Good morning my lovely french friends!', 'en', 'fr')
        # get access token
        params = urlencode({
            'client_id': MS_TRANSLATOR_CLIENT_ID,
            'client_secret': MS_TRANSLATOR_CLIENT_SECRET,
            'scope': 'http://api.microsofttranslator.com', 
            'grant_type': 'client_credentials'})
        conn = httplib.HTTPSConnection("datamarket.accesscontrol.windows.net")
        conn.request("POST", "/v2/OAuth2-13", params)
        response = json.loads (conn.getresponse().read().decode('utf-8'))
        token = response[u'access_token']

        # translate
        conn = httplib.HTTPConnection('api.microsofttranslator.com')
        params = {'appId': 'Bearer ' + token,
                  'from': sourceLang,
                  'to': destLang,
                  'text': text.encode("utf-8")}
        conn.request("GET", '/V2/Ajax.svc/Translate?' + urlencode(params))
        # jsonStr = "{\"response\":" + conn.getresponse().read().decode('utf-8') + "}"
        # response = json.loads(jsonStr)
        # return response
        # return response["response"]
        return conn.getresponse().read().decode('utf-8')
    except:
        return traceback.format_exc()
        return gettext('Error: Unexpected error.')
