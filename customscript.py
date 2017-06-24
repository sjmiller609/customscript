#!/usr/bin/env python

import sys
password = sys.argv[1]
with open("C:\\password.txt","w") as f:
    f.write(password)

data = """

import xlrd
import os
import sys
import json
import time
import datetime
import pyautogui
import requests
import base64
import re
from random import randint
import sendgrid
from sendgrid.helpers.mail import *

def wait_until(dt):
    while(dt > datetime.datetime.today()):
        time.sleep(30)

def get_public_ip():
    response = requests.get("https://www.google.com/search?num=100&safe=off&site=webhp&source=hp&q=whats+my+ip&oq=whats+my+ip")
    re_ipv4= re.compile(">((?:[0-9]{1,3}\.){3}[0-9]{1,3})<")
    ip = re_ipv4.findall(response.text)
    return ip[0]

def send_picture(email,my_ip):
    root_path = os.path.dirname(os.path.realpath(__file__))
    pyautogui.screenshot(root_path+"checkouts.png")
    time.sleep(0.1)
    sg = sendgrid.SendGridAPIClient(apikey='')
    from_email = Email("steven@shoemoney.com")
    subject = my_ip
    to_email = Email(email)
    content = Content("text/plain", "Hello, Email!")
    message = Mail(from_email, subject, to_email, content)
    attachment= Attachment()
    with open(root_path+"checkouts.png",'rb') as f:
        encoded = base64.b64encode(f.read()).decode()
    attachment.content = encoded
    attachment.type = 'image/png'
    attachment.filename = 'checkouts.png'
    message.add_attachment(attachment)
    stuff = message.get()
    response = sg.client.mail.send.post(request_body=stuff)
    print(response.status_code)
    print(response.body)
    print(response.headers)

def start_release(pic):
    #left, top, width, height = pyautogui.locateOnScreen(pic)
    if "FTL.png" in pic:
        pyautogui.click((999,248))
        pyautogui.click((999,248))
    if "FA.png" in pic:
        pyautogui.click((999,277))
        pyautogui.click((999,277))
    if "EB.png" in pic:
        pyautogui.click((999,311))
        pyautogui.click((999,311))
    if "Champs.png" in pic:
        pyautogui.click((999,344))
        pyautogui.click((999,344))

    print("matched a release button to picture")
    #pyautogui.click((left,top))
    #pyautogui.click((left,top))
    #time.sleep(2)   
    pyautogui.click((1004,157))
    #time.sleep(1)

def get_release_pics():
    root_path = os.path.dirname(os.path.realpath(__file__))
    result = ["\\\\FTL.png","\\\\FA.png","\\\\EB.png","\\\\Champs.png"]
    result = [root_path+x for x in result]
    return result

def open_slayer(activation_key):
    print("opening sole slayer")
    ssfilename = "C:\\\\Program Files (x86)\\\\SoleSlayer\\\\SoleSlayer"
    os.startfile(ssfilename)
    time.sleep(15)
    pyautogui.typewrite(activation_key)
    time.sleep(4)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.hotkey("win","right")
    time.sleep(1)

def click_away():
    pyautogui.click(x=1203,y=581)
    pyautogui.click(x=846,y=686)
    time.sleep(0.1)

def open_success_monitor():
    pyautogui.click((1832,122))

def get_seed(n=32):
  range_start = 10**(n-1)
  range_end = (10**n)-1
  return randint(range_start, range_end)

def format_json(json_in):
    return json.dumps(json_in,indent=2, separators=(',',': '))

def pretty_print(json_in):
  print(format(json_in))

def get_checkout_by_index(checkout_profiles,index):
    for profile in checkout_profiles:
        if profile["index"] == index:
            return profile
    return None

#get data from server
with open("C:\\\\password.txt","r") as f:
    password = f.read()
print("get license data")
response = requests.post("http://13.90.151.174:8080/releaseinfo",json={"password":password})
print(response)
payload = response.json()
license = payload["license"]
release_profiles = payload["release_profiles"]
all_checkout_profiles = payload["all_checkout_profiles"]
print(license)

print("getting public ip")
public_ip = get_public_ip()
print(public_ip)

checkout_profiles = []
for checkout_index in release_profiles[0]["tasks"]:
    checkout_profiles.append(get_checkout_by_index(all_checkout_profiles,checkout_index["checkoutprofile"]))

for rprofile in release_profiles:
    for checkout_id in rprofile["tasks"]:
        if not get_checkout_by_index(checkout_profiles,checkout_id["checkoutprofile"]):
            print("ERROR: did not have checkoutprofile with index: "+checkout_id["checkoutprofile"])
            exit(1)

data_dir = os.path.expanduser("~")+'\\\\AppData\\\\Local\\\\SoleSlayer\\\\'
print(data_dir)
try:
    os.makedirs(data_dir)
except:
    pass

with open(data_dir+"releaseprofiles.json","w") as f:
    f.write(format_json(release_profiles))

with open(data_dir+"checkoutprofiles.json","w") as f:
    f.write(format_json(checkout_profiles))

activation_key = license
open_slayer(activation_key)
click_away()

releases = get_release_pics()

for rel in releases:
    start_release(rel)

print("opening success monitor")
open_success_monitor()

quit()
print("waiting until after the release is over")
wait_until(datetime.datetime(2017,4,29,10,0,0,0))
while True:
    send_picture("sjmiller609@gmail.com",public_ip)
    #send_picture("gregcron@gmail.com",public_ip)
    time.sleep(20*60)
"""

with open("C:\\start_slayer.py","w") as f:
    f.write(data)

exit(0)
