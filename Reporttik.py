#Faraaaaaa
#telegram:Wu3xq
#channel: https://t.me/TEAM_1780
import requests
import random
import time
from threading import Lock
import os

os.system("start https://t.me/TEAM_1780")

PRNT = Lock()
red = "\033[1;31;40m"
grn = '\033[1;32;40m'
yel = '\033[1;33;40m'
wit = "\033[1;37;40m"
bloFT = "\033[1;36;40m"

def vv1ck(*a, **b):
    with PRNT:
        print(*a, **b)
        
def display_banner():
    banner = """
FARA
@Wu3xq
Version: v1
"""
    vv1ck(bloFT + banner)

def generate_device_id():
    return str(random.randint(1000000000000000000, 9999999999999999999))

def generate_user_agent():
    ios_versions = ["14.6", "14.7", "14.8", "15.0", "15.1"]
    return f"TikTok 17.6.1 rv:176111 (iPhone; iOS {random.choice(ios_versions)}; ar_JO@numbers=latn) Cronet"

def send_report(username, sessionid, proxy=None):
    url = f'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/aweme/feedback/?version_code=17.6.1&language=ar&app_name=musical_ly&app_version=17.6.1&vid=A0E47A34-1BAE-4407-AB86-219468E804C5&residence=JO&device_id={generate_device_id()}&channel=App%20Store&mcc_mnc=41601&carrier_region=JO&tz_offset=10800&op_region=JO&aid=1233&locale=ar&sys_region=JO&account_region=&screen_width=1125&uoo=1&openudid=62b064ef098f5d1c5817b2bf68f0ce3be9a52dcf&cdid=C3303766-D942-4770-B538-DADCC78137C4&os_api=18&ac=WIFI&os_version=14.6&app_language=ar&content_language=&tz_name=Asia/Amman&current_region=JO&device_platform=iphone&build_number=176111&iid=7090067468483643138&device_type=iPhone11,2&idfa=00000000-0000-0000-0000-000000000000&reporter_id=6858802024084784129&reason=3024&uri=&report_type=user&enter_from=&object_id={username}&request_tag_from=h5&report_desc=helpful&owner_id={username}'

    headers = {
        'Host': 'api16-normal-c-alisg.tiktokv.com',
        'Connection': 'keep-alive',
        'sdk-version': '2',
        'passport-sdk-version': '5.12.1',
        'x-Tt-Token': '01e7331d3b2acff63235e08ce65a056ffe00f5e3ca7fcea56e4439274cbdb58a56d0ea37f92f2923cdc0814764e4d46983264d873707430d26340660a85e4b4ec1439397f36afd207addd1b44a32ff3723070b8e6295ebd46c7886703ef18abc44e0b-1.0.1',
        'User-Agent': generate_user_agent(),
        'x-tt-store-idc': 'alisg',
        'x-tt-store-region': 'jo',
        'X-SS-DP': '1233',
        'x-tt-trace-id': '00-5a75f57410612f2097560d46060b04d1-5a75f57410612f20-01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': f'sessionid:{sessionid}',
        'X-Khronos': str(int(time.time())),
        'X-Gorgon': '8402408660004c06eadd0143f42058e4d04984020125fdb0d7d9'
    }

    if proxy:
        proxies = {
            "http": proxy,
            "https": proxy
        }
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        except Exception as e:
            vv1ck(red + f"Error with proxy {proxy}: {e}")
            return False
    else:
        try:
            response = requests.get(url, headers=headers, timeout=10)
        except Exception as e:
            vv1ck(red + f"Error: {e}")
            return False

    if response.status_code == 200:
        vv1ck(grn + f"Report successfully sent for username: {username}")
        return True
    else:
        vv1ck(red + f"Failed to send report for {username}. Status: {response.status_code} Response: {response.text}")
        return False

def send_multiple_reports(username, sessionid, report_count, proxy=None):
    success_count = 0
    for _ in range(report_count):
        if send_report(username, sessionid, proxy):
            success_count += 1
        time.sleep(2) 
    chyooo(wit + f"\nTotal successful reports: {success_count}/{report_count}")

def display_banner():
    banner = """
Report
"""
    chyooo(bloFT + banner)

if __name__ == "__main__":
    sessionid = input(wit + "Enter your session ID: ")
    username = input(wit + "Enter the target username: ")
    report_count = int(input(wit + "How many reports do you want to send?: "))
    
    print(yel + "Choose reporting method:")
    print("1. Auto Report By Device ID (📱)")
    print("2. Auto Report By Proxy File (🔥)")
    method = input(wit + "Select an option (1 or 2): ")

    if method == "2":
        proxy_file = input(wit + "Enter the path to your proxy file: ")
        with open(proxy_file, 'r') as f:
            proxies = f.read().splitlines()

        for _ in range(report_count):
            proxy = random.choice(proxies)
            send_multiple_reports(username, sessionid, 1, proxy)
    else:
        send_multiple_reports(username, sessionid, report_count)

    display_banner()
    #coded by chyooo