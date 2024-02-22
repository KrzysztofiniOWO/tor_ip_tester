import time
import requests
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

repeats = int(input("How many requests you want to make?: "))

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

def make_tor_requests():
    for _ in range(repeats):
        headers = { 'User-Agent': UserAgent().random }
        time.sleep(10)
        with Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal(Signal.NEWNYM)
            response = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies)
            ip_address = response.json()["origin"]
            result = f"IP Address: {ip_address}\n"
            save_results(result)

def save_results(result):
    with open("results.txt", 'a') as file:
        file.write(result)

make_tor_requests()
