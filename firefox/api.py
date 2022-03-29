from email import message
from httpcore import request


import requests
import json

url = 'https://onlinesim.ru/api/getFreeMessageList?cpage=1&phone=9775593886&country=7'

message_list = []

def main():
    r =requests.get(url)
    data = r.json()
    message = data['messages']['data']
    for data in message:
        text = data['text']
    
        message_list.append({
                'text': [text]
            })

    with open('data.json', 'w', encoding='UTF-8') as f:
        json.dump(message_list, f, indent=4,ensure_ascii=False)

main()