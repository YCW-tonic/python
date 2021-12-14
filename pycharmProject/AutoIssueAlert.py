import json
import logging

import urlfetch
from bs4 import BeautifulSoup
import requests
from time import sleep

# url = "https://en.wikipedia.org/wiki/Main_Page"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# for anchor in soup.find_all('a'):
#     print(anchor.get('href', '/'))

# beautifulsoap取label值-->TESTED
url = "http://10.192.5.49/wcdb/aic/aic001.aspx?ITOnly=IT"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# for i in soup.find_all('span'):
#     print(i.get_text())
soupItem = soup.find('span', {'id': 'lab_ITalert'})
print(soupItem.get_text()[:1])

isSend = False
while True:
    try:
        if soupItem.get_text()[:1] != "T":
            if not isSend:
                print(isSend)
                url = 'https://fcm.googleapis.com/fcm/send'
                body = {
                    "condition": "'test' in topics",
                    "priority": "high",
                    "content_available": True,
                    "notification": {
                        "title": "自動發料異常",
                        "body": "AL超過5筆"
                    }
                }

                headers = {"Content-Type": "application/json",
                           "Authorization": "key=AAAA94blMKI:APA91bGGQVvCmus04xekIy0lHZAOA2DVjBN38hTxJCSPWM3-KP9AcLBEoAc-OfqD8_ebOH5d_5Y4IFw62nY6mcEXg0hkTQNG17C17xxzdU3MDKrlFi6j81b2bLvUnEpwvPnDAlItKlTe"}

                ret = requests.post(url, data=json.dumps(body), headers=headers)
                print(ret.status_code)
                print(ret.content)
                isSend = True
                print("Label start with A")
            else:#isSend是True
                print("do nothing & Label start with A")
        else:  # label是T開頭
            isSend = False
            print("do nothing & Lable start with T")

    except Exception as e:
        print(e)
    sleep(60)
