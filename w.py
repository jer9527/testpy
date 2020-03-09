import requests,time
from twilio.rest import Client

phone = r'+8618006226827'
URL = r'http://222.92.197.179:9001/Front'

website = True
try_times = 0

def web_code(url):
    web_info = requests.get(url)
    web_info.encoding = web_info.apparent_encoding
    #if web_info.status_code == 200:
    if '53' not in web_info.text:
        sent_msm(phone,URL + " is OK now !!!")
        website = False
    else:
        pass


def sent_msm(phone_num, smstext):
    account_id = r'AC0efd9cf0af373bba7a4942b7ad65def6'
    auth_token = r'c5daf9718f3f34790d506bbef1be7e0f'
    client = Client(account_id, auth_token)
    message = client.messages.create(
        to=phone_num,
        from_='+12408959735',  # 官方提供号码
        body=smstext
    )
    print(message.sid)


if __name__ == "__main__":
    while website == True:
        web_code(URL)
        time.sleep(500)
        try_times = try_times + 1
        print('已经尝试了 ',try_times)

    
