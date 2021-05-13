from onlinesimru import GetFree, GetRent, GetUser, GetNumbers
import json
import requests

with open('key.json', 'r', encoding='utf-8') as setting:
    data = json.load(setting)
    token = data['key']

phone_dict = {}

def main():
    client = GetUser(token)
    balance = client.balance()
    print(balance['balance'])

def phone_generator():
    global phone_dict
    phone = {}
    r = requests.get('https://onlinesim.ru/api/getNum.php?', json=data)
    response = json.loads(r.text)
    if response['response'] == 1:
        phone[response['number']] = response['tzid']
        phone_dict.update(phone)
    elif response['response'] == 'NO_NUMBER':
        print('该地区无可用电话号码，请更换地区')
    else:
        print('也许是余额不足了')
    print(phone_dict)

def get_code():
    get_state = requests.get('https://onlinesim.ru/api/getState.php', params={'api': token})
    print(get_state.text)

# main()
# phone_generator()
get_code()

