import urllib.request
import json
import requests
import datetime

import settings

FOLDER_ID = "b1g6qkn8je10ca0ud4gp"  # Идентификатор каталога
IAM_TOKEN = dict.fromkeys(('key', 'made'))
IAM_TOKEN['made'] = datetime.datetime.now()-datetime.timedelta(hours=11)


def getIamToken(oauth_token):
    data = {"yandexPassportOauthToken": oauth_token}
    resp = requests.post("https://iam.api.cloud.yandex.net/iam/v1/tokens", data=json.dumps(data))

    decodedData = json.loads(resp.text)
    if decodedData.get("error_code") is None:
        return decodedData.get("iamToken")
    return ''


def asrPostProc(res):
    res = res.lower().replace('умнож', ' * ')
    res = res.replace('дел', ' / ')
    res = res.replace('степен', ' ^ ')
    for l in 'абвгдеёжзийклмнопрстуфхцчшщыъьэюя ':
        res = res.replace(l, '')
    return res


def getAsrRes(content):
    params = "&".join([
        "topic=general",
        "folderId=%s" % FOLDER_ID,
        "lang=ru-RU"
    ])

    if (datetime.datetime.now() - IAM_TOKEN.get('made')).seconds > 2*60*60:
        IAM_TOKEN['key'] = getIamToken(settings.ya_oauth)
        IAM_TOKEN['made'] = datetime.datetime.now()
        print('IAM_TOKEN updated')
        print(IAM_TOKEN)

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=content)
    url.add_header("Authorization", "Bearer %s" % IAM_TOKEN.get('key'))

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    res = ''
    print(decodedData)
    if decodedData.get("error_code") is None:
        res = decodedData.get("result")
    return res
