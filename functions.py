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

def make_tor_requests_diff_ip(repeats):
    for _ in range(repeats):
        headers = { 'User-Agent': UserAgent().random }
        time.sleep(10)
        with Controller.from_port(port=9051) as c:
            start_time = time.time()
            c.authenticate()
            c.signal(Signal.NEWNYM)
            response = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies)
            end_time = time.time()
            total_time = end_time - start_time
            ip_address = response.json()["origin"]
            result = f"IP Address: {ip_address}, " + f"{total_time}, " + f"{response.status_code}\n"
            save_requests_results(result)

def make_tor_requests_same_ip(repeats):
    for _ in range(repeats):
        start_time = time.time()
        response = requests.get("http://httpbin.org/ip", proxies=proxies)
        end_time = time.time()
        total_time = end_time - start_time
        ip_address = response.json()["origin"]
        result = f"IP Address: {ip_address}, " + f"{total_time}, " + f"{response.status_code}\n"
        save_requests_results(result)

def check_first_image_load_time_diff_ip(repeats):
    for _ in range(repeats):
        headers = { 'User-Agent': UserAgent().random }
        time.sleep(10)
        with Controller.from_port(port=9051) as c:
            start_time = time.time()
            c.authenticate()
            c.signal(Signal.NEWNYM)
            response = requests.get("https://www.wp.pl/", headers=headers, proxies=proxies)
            soup = bs(response.content, 'html.parser')
            first_image = soup.find('img')
            if first_image:
                image_url = first_image['src']
                start_time = time.time()
                image_response = requests.get(image_url)
                end_time = time.time()
                total_time = end_time - start_time
                save_image(image_response.content)
                return total_time
            else:
                print("Image could not be found")
                return None


def check_first_image_load_time_same_ip(repeats):
    for _ in range(repeats):
        start_time = time.time()
        response = requests.get("https://www.wp.pl/", proxies=proxies)
        soup = bs(response.content, 'html.parser')
        first_image = soup.find('img')
        if first_image:
            image_url = first_image['src']
            start_time = time.time()
            image_response = requests.get(image_url)
            end_time = time.time()
            total_time = end_time - start_time
            save_image(image_response.content)
            return total_time
        else:
            print("Image could not be found")
            return None
        

def save_requests_results(result):
    with open("request_results.txt", 'a') as file:
        file.write(result)

def save_image(image_data):
    with open('saved_image.jpg', 'wb') as f:
        f.write(image_data)
    print("Image saved as saved_image.jpg")