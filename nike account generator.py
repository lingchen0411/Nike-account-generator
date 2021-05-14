import json
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import string
import names

with open('proxies.txt', 'r') as p:
    proxies = p.readlines()
    proxy = proxies[random.randint(0, len(proxies)-1)]

def generator():
    chrome_options = Options()
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    broswer = webdriver.Chrome(chrome_options=chrome_options)

    broswer.get('https://www.nike.com/gb/register')
    broswer.implicitly_wait(7)

    # cookie setting
    broswer.find_element_by_xpath('//*[@data-var="acceptBtn"]').click()

    email = ''.join(random.sample(string.ascii_letters, random.randint(6, 10))) + '@lingchen888.com'
    broswer.find_element_by_xpath('//*[@type="email"]').send_keys(email)
    password = ''.join(random.sample(string.ascii_letters + string.digits, 12))
    broswer.find_element_by_xpath('//*[@type="password"]').send_keys(password)
    first_name = names.get_first_name()
    broswer.find_element_by_xpath('//*[@placeholder="First Name"]').send_keys(first_name)
    last_name = names.get_last_name()
    broswer.find_element_by_xpath('//*[@placeholder="Last Name"]').send_keys(last_name)

    actions = ActionChains(broswer)
    broswer.find_element_by_xpath('//*[@placeholder="Date of Birth"]').click()
    year = random.randint(1990, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    actions.send_keys(year, Keys.TAB)
    actions.send_keys(month)
    actions.send_keys(day)
    actions.perform()

    broswer.find_element_by_xpath('//*[@class="checkbox"]').click()
    broswer.find_element_by_xpath('//div//span[contains(text(), "Male")]').click()

    df_account = pd.read_csv('NikeAccount.csv')
    colNames = df_account.columns
    new_account = [[email, password, proxy, 'gb', first_name, last_name, '', '', str(year)+'/'+str(month)+'/'+str(day), '']]
    df_new_account = pd.DataFrame(data=new_account, columns=colNames)
    df_complete = pd.concat([df_account, df_new_account], axis=0)
    # df_complete.to_csv('NikeAccount.csv')

    broswer.find_element_by_xpath('//*[@value="JOIN US"]').click()
    time.sleep(120)

generator()

