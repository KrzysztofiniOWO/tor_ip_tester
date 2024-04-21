import time
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

def change_ip():
    time.sleep(10)
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

def make_tor_request(url, headers, proxies):
    start_time = time.time()
    response = requests.get(url, headers=headers, proxies=proxies)
    end_time = time.time()
    total_time = end_time - start_time
    return response, total_time


def make_tor_requests_diff_ip(webpage, amount, path):
    for _ in range(amount):
        headers = { 'User-Agent': UserAgent().random }
        change_ip()
        response, total_time = make_tor_request(webpage, headers, proxies)
        my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
        result = f"IP Address: {my_ip}, " + f"{total_time}, " + f"{response.status_code}" + f" {webpage}\n"
        name = f"{path}/results_diff_ip.txt"
        save_requests_results(result, name)


def make_tor_requests_same_ip(webpage, amount, path):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        response, total_time = make_tor_request(webpage, headers, proxies)
        my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
        result = f"IP Address: {my_ip}, " + f"{total_time}, " + f"{response.status_code}" + f" {webpage}\n"
        name = f"{path}/results_same_ip.txt"
        save_requests_results(result, name)


def check_first_image_load_time_diff_ip(webpage, amount, path):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        change_ip()
        response, _ = make_tor_request(webpage, headers, proxies)
        soup = bs(response.content, 'html.parser')
        first_image = soup.find('img')
        if first_image:
            image_url = first_image['src']
            _, total_time = make_tor_request(image_url, headers, proxies)
            print(f"image load time diff ip {total_time}")
            location = f"{path}/img_diff_ip_{repeat}.jpg"
            save_image(response.content, location)
            print(total_time)
        else:
            print("Image could not be found")


def check_first_image_load_time_same_ip(webpage, amount, path):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        response, _ = make_tor_request(webpage, headers, proxies)
        soup = bs(response.content, 'html.parser')
        first_image = soup.find('img')
        if first_image:
            image_url = first_image['src']
            _, total_time = make_tor_request(image_url, headers, proxies)
            print(f"image load time same ip {total_time}")
            location = f"{path}/img_same_ip_{repeat}.jpg"
            save_image(response.content, location)
            print(total_time)
        else:
            print("Image could not be found")
        

def save_requests_results(result, name):
    with open(name, 'a') as file:
        file.write(result)

def save_image(image_data, location):
    with open(location, 'wb') as f:
        f.write(image_data)