import time
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
import ftplib
import dns.resolver
import asyncio
import websockets

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
    response = requests.get(url, headers=headers, proxies=proxies)
    return response

def test_mongodb_query(uri, dbname, collection_name, query):
    client = MongoClient(uri)
    db = client[dbname]
    collection = db[collection_name]
    start_time = time.time()
    result = collection.find_one(query)
    end_time = time.time()
    total_time = end_time - start_time
    client.close()
    return total_time

def upload_file_ftp(server, username, password, file_path):
    try:
        ftp = ftplib.FTP(server)
        ftp.login(username, password)
        with open(file_path, 'rb') as file:
            start_time = time.time()
            ftp.storbinary(f'STOR {file_path}', file)
            end_time = time.time()
        ftp.quit()
        return end_time - start_time
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        return None


def fetch_post(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
async def websocket_test(uri):
    async with websockets.connect(uri) as websocket:
        start_time = time.perf_counter()
        await websocket.send("Hello, WebSocket!")
        response = await websocket.recv()
        end_time = time.perf_counter()
        return end_time - start_time, response
    
def get_save_data_and_save(path, additional_content, headers, total_time, filename):
    my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
    result = f"{my_ip}, " + f"{total_time}, " + additional_content
    result_file_name = f"{path}" + filename
    save_results(result, result_file_name)

    
def make_tor_requests_diff_ip(webpage, amount, path_results):
    for _ in range(amount):
        headers = { 'User-Agent': UserAgent().random }
        change_ip()
        start_time = time.time()
        response = make_tor_request(webpage, headers, proxies)
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{response.status_code}, {webpage}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/ping_results_diff_ip.txt")

def make_tor_requests_same_ip(webpage, amount, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        start_time = time.time()
        response = make_tor_request(webpage, headers, proxies)
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{response.status_code}, {webpage}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/ping_results_same_ip.txt")

def check_first_image_download_time_diff_ip(webpage, amount, path_results, path_download):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        change_ip()
        response = make_tor_request(webpage, headers, proxies)
        soup = bs(response.content, 'html.parser')
        first_image = soup.find('img')
        if first_image:
            start_time = time.time()
            img_url = first_image['src']
            response_image = make_tor_request(img_url, headers, proxies)
            location = f"{path_download}/img_diff_ip_{repeat}.jpg"
            save_image(response_image.content, location)
            end_time = time.time()
            total_time = end_time - start_time
            additional_content = f"{response.status_code}, {webpage}\n"
            get_save_data_and_save(path_results, additional_content, headers, total_time, "/image_dl_results_diff_ip.txt")
        else:
            print("Image could not be found")

def check_first_image_download_time_same_ip(webpage, amount, path_results, path_download):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        response = make_tor_request(webpage, headers, proxies)
        soup = bs(response.content, 'html.parser')
        first_image = soup.find('img')
        if first_image:
            start_time = time.time()
            img_url = first_image['src']
            response_image = make_tor_request(img_url, headers, proxies)
            location = f"{path_download}/img_same_ip_{repeat}.jpg"
            save_image(response_image.content, location)
            end_time = time.time()
            total_time = end_time - start_time
            additional_content = f"{response.status_code}, {webpage}\n"
            get_save_data_and_save(path_results, additional_content, headers, total_time, "/image_dl_results_same_ip.txt")
        else:
            print("Image could not be found")

def test_mongodb_diff_ip(amount, path_results, db_config, query):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        change_ip()
        total_time = test_mongodb_query(db_config['uri'], db_config['dbname'], db_config['collection'], query)
        additional_content = "\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/mongodb_results_diff_ip.txt")

def test_mongodb_same_ip(amount, path_results, db_config, query):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        total_time = test_mongodb_query(db_config['uri'], db_config['dbname'], db_config['collection'], query)
        additional_content = "\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/mongodb_results_same_ip.txt")

def download_file_diff_ip(webpage, amount, path_results, path_download):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        change_ip()
        response = requests.get(webpage, headers=headers, proxies=proxies)
        
        soup = bs(response.content, 'html.parser')
        download_link = soup.find('a', class_='download_text', href="text/Sample-text-file-1000kb.txt")
        
        if download_link:
            file_url = f"https://sample-videos.com/{download_link['href']}"
            file_name = f'{repeat}' + 'diff_ip_' + download_link['download']
            
            start_time = time.time()
            response_file = make_tor_request(file_url, headers, proxies)
            
            with open(f"{path_download}/{file_name}", 'wb') as f:
                for chunk in response_file.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

            end_time = time.time()
            total_time = end_time - start_time
            additional_content = f"{response_file.status_code}, {file_url}\n"
            get_save_data_and_save(path_results, additional_content, headers, total_time, "/file_dl_results_diff_ip.txt")
            
        else:
            print("Download link not found")

def download_file_same_ip(webpage, amount, path_results, path_download):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        response = requests.get(webpage, headers=headers, proxies=proxies)
        
        soup = bs(response.content, 'html.parser')
        download_link = soup.find('a', class_='download_text', href="text/Sample-text-file-1000kb.txt")
        
        if download_link:
            file_url = f"https://sample-videos.com/{download_link['href']}"
            file_name = f'{repeat}' + 'same_ip_' + download_link['download']
            
            start_time = time.time()
            response_file = make_tor_request(file_url, headers, proxies)
            
            with open(f"{path_download}/{file_name}", 'wb') as f:
                for chunk in response_file.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            
            end_time = time.time()
            total_time = end_time - start_time
            additional_content = f"{response_file.status_code}, {file_url}\n"
            get_save_data_and_save(path_results, additional_content, headers, total_time, "/file_dl_results_same_ip.txt")
            
        else:
            print("Download link not found")

def test_upload_file_ftp_diff_ip(server, username, password, amount, file_path, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        change_ip()
        total_time = upload_file_ftp(server, username, password, file_path)
        if total_time:
            additional_content = "\n"
            get_save_data_and_save(path_results, additional_content, headers, total_time, "/ftp_upload_diff_ip.txt")

        else:
            print("Failed to upload file")

def test_upload_file_ftp_same_ip(server, username, password, amount, file_path, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        total_time = upload_file_ftp(server, username, password, file_path)
        if total_time:
            additional_content = "\n"
            get_save_data_and_save(path_results, additional_content, headers, total_time, "/ftp_upload_same_ip.txt")

        else:
            print("Failed to upload file")

def test_jsonplaceholder_get_diff_ip(amount, path_results):
    base_url = 'https://jsonplaceholder.typicode.com'
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        change_ip()
        start_time = time.time()
        json_data = fetch_post(f"{base_url}/posts/1")
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{json_data}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/jsonplaceholder_get_diff_ip.txt")

def test_jsonplaceholder_get_same_ip(amount, path_results):
    base_url = 'https://jsonplaceholder.typicode.com'
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        start_time = time.time()
        json_data = fetch_post(f"{base_url}/posts/1")
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{json_data}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/jsonplaceholder_get_same_ip.txt")

def test_dns_resolution_diff_ip(domain, num_tests, path_results):
    headers = {'User-Agent': UserAgent().random}
    for _ in range(num_tests):
        change_ip()
        start_time = time.time()
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']
        answer = resolver.query(domain)
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"Answer: {answer[0].to_text()}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/dns_resolution_name_diff_ip.txt")

def test_dns_resolution_same_ip(domain, num_tests, path_results):
    headers = {'User-Agent': UserAgent().random}
    for _ in range(num_tests):
        start_time = time.time()
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']
        answer = resolver.query(domain)
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"Answer: {answer[0].to_text()}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/dns_resolution_name_same_ip.txt")

def test_websocket_diff_ip(uri, amount, path_results):
    for _ in range(amount):
        change_ip()
        headers = {'User-Agent': UserAgent().random}
        total_time, response = asyncio.run(websocket_test(uri))

        additional_content = f"Response: {response}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/websocket_results_diff_ip.txt")

def test_websocket_same_ip(uri, amount, path_results):
    headers = {'User-Agent': UserAgent().random}
    for _ in range(amount):
        total_time, response = asyncio.run(websocket_test(uri))

        additional_content = f"Response: {response}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/websocket_results_same_ip.txt")
        
def save_results(result, name):
    with open(name, 'a') as file:
        file.write(result)

def save_image(image_data, location):
    with open(location, 'wb') as f:
        f.write(image_data)