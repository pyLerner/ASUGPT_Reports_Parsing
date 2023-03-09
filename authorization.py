import requests

# URL's const's
MAIN_URL = "https://prod.gpt.adc.spb.ru/Transport/main/?app=complete"
AUTH_URL = "https://prod.gpt.adc.spb.ru/Transport/main/publicService/Security"

# Other const's
session_id = ''
cookie = f'JSESSIONID={session_id}; https%3A%2F%2Fprod.gpt.adc.spb.ru%2FTransport%2Fmain%2Ftheme=%7B%22state%22%3A%7B%22id%22%3A%22s%3Aslate%22%2C%20%22file%22%3A%22s%3Agxt%2Fthemes%2Fslate%2Fcss%2Fxtheme-slate.css%22%7D%7D'
content_type = 'text/x-gwt-rpc; charset=utf-8'   
headers = {
        'Content-Type': content_type,
        'Cookie': cookie,
    }

# Получаем session_id для авторизации
def get_session_id():
    session_id = requests.get(MAIN_URL)
    session_id = session_id.cookies["JSESSIONID"]
    print(session_id)
    return session_id

# Авторизация и получаем session_id2 для работы во время сессии
def auth(session_id, content_type, cookie, headers):
    payload = "7|0|7|https://prod.gpt.adc.spb.ru/Transport/main/|A1F667AC81EE84A38F9D07D02A55C4A0|ru.csbi.transport.gwtapp.client.SecurityService|login|java.lang.String/2004016611|akishbaya|123456|1|2|3|4|2|5|5|6|7|"
    content_type = content_type
    cookie = cookie
    headers = headers

    auth = requests.post(AUTH_URL, headers=headers, data=payload)
    session_id = auth.cookies["JSESSIONID"]
    print(session_id)
    return session_id
