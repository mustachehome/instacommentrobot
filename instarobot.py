


import json
import time
from dataclasses import dataclass

import libs
import requests
from selenium import webdriver

browser=webdriver.Chrome()
browser.get("https://www.instagram.com/")
time.sleep(5)

username=browser.find_element("name","username")
password=browser.find_element("name","password")
username.send_keys("mustachehomenft")
password.send_keys("24012019HSk")
time.sleep(5)
login=browser.find_element("xpath", "//*[@id='loginForm']/div/div[3]/button/div")
login.click()
time.sleep(5)

##post shortcode tanımlanan alan. eğer postun linki bu ise  https://www.instagram.com/p/CECXW9bsRzo/ , shortcode budur CECXW9bsRzo
shortcode = "Cdqo_CpKANC"
url = 'https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables=%7B"shortcode":"'+shortcode+'","first":50,"after":"0"%7D'
r = requests.get(url)
data = json.loads(r.text)

end_cursor = data['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']

def fetch_data(shortcode,token):
    url = 'https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables=%7B"shortcode":"'+shortcode+'","first":50,"after":"'+token+'"%7D'
    r = requests.get(url)
    b = json.loads(r.text)
    cursor = b['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']
    data = b['data']['shortcode_media']['edge_media_to_comment']['edges']
    for x in data:
        ## bu kullanıcı adını verir
        a=x['node']['owner']['username']
        print(a)
    while cursor != "null":
       return fetch_data(shortcode,cursor)

fetch_data(shortcode,"0")
