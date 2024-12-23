import utils
import config
import time
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from urllib.parse import urljoin
import websocket

def make_tor_request(url, headers, proxies):
    response = requests.get(url, headers=headers, proxies=proxies)
    return response

def get_save_data_and_save(path, additional_content, headers, total_time, filename):
    my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=config.proxies).json()["origin"]
    result = f"{my_ip}, " + f"{total_time}, " + additional_content
    result_file_name = f"{path}" + filename
    print(result_file_name)
    save_results(result, result_file_name)

def save_results(result, name):
    with open(name, 'a') as file:
        file.write(result)

def save_image(image_data, location):
    with open(location, 'wb') as f:
        f.write(image_data)
    
def make_pings_diff_ip(webpage, amount, path_results):
    for _ in range(amount):
        headers = { 'User-Agent': UserAgent().random }
        utils.change_ip()
        start_time = time.time()
        response = make_tor_request(webpage, headers, config.proxies)
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{response.status_code}, {webpage}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/ping_results_diff_ip.txt")

def make_pings_same_ip(webpage, amount, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        start_time = time.time()
        response = make_tor_request(webpage, headers, config.proxies)
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{response.status_code}, {webpage}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/ping_results_same_ip.txt")

def check_first_image_download_time_diff_ip(webpage, amount, path_results, path_download):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        utils.change_ip()
        
        response = make_tor_request(webpage, headers, config.proxies)
        soup = bs(response.content, 'html.parser')
        first_image = None

        for img in soup.find_all('img'):
            img_url = img['src']
            if img_url.endswith(('.jpg', '.jpeg', '.svg', '.png')):
                first_image = img
                break

        if first_image:
            start_time = time.time()
            img_url = urljoin(webpage, first_image['src'])
            file_extension = img_url.split('.')[-1]
            
            response_image = make_tor_request(img_url, headers, config.proxies)
            location = f"{path_download}/img_diff_ip_{repeat}.{file_extension}"
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
        
        response = make_tor_request(webpage, headers, config.proxies)
        soup = bs(response.content, 'html.parser')
        first_image = None

        for img in soup.find_all('img'):
            img_url = img['src']
            if img_url.endswith(('.jpg', '.jpeg', '.svg', '.png')):
                first_image = img
                break

        if first_image:
            start_time = time.time()
            img_url = urljoin(webpage, first_image['src'])
            file_extension = img_url.split('.')[-1]
            
            response_image = make_tor_request(img_url, headers, config.proxies)
            location = f"{path_download}/img_same_ip_{repeat}.{file_extension}"
            save_image(response_image.content, location)
            
            end_time = time.time()
            total_time = end_time - start_time
            
            additional_content = f"{response.status_code}, {webpage}\n"
            get_save_data_and_save(path_results, additional_content, headers, total_time, "/image_dl_results_same_ip.txt")
        else:
            print("Image could not be found")

def download_file_diff_ip(webpage, amount, path_results, path_download):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        utils.change_ip()
        response = requests.get(webpage, headers=headers, proxies=config.proxies)
        
        soup = bs(response.content, 'html.parser')
        download_link = soup.find('a', class_='text-sm pt-2 pb-2 pr-4 pl-4 rounded bg-gray-700 hover:bg-gray-800 text-white md:w-full md:text-center', href=True)
        
        if download_link:
            file_url = f"https://filesampleshub.com{download_link['href']}"
            file_name = f'{repeat}' + '_diff_ip_' + download_link['href'].split('/')[-1]
            
            start_time = time.time()
            response_file = make_tor_request(file_url, headers, config.proxies)
            
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
        response = requests.get(webpage, headers=headers, proxies=config.proxies)
        
        soup = bs(response.content, 'html.parser')
        download_link = soup.find('a', class_='text-sm pt-2 pb-2 pr-4 pl-4 rounded bg-gray-700 hover:bg-gray-800 text-white md:w-full md:text-center', href=True)
        
        if download_link:
            file_url = f"https://filesampleshub.com{download_link['href']}"
            file_name = f'{repeat}' + '_same_ip_' + download_link['href'].split('/')[-1]
            
            start_time = time.time()
            response_file = make_tor_request(file_url, headers, config.proxies)
            
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

def test_jsonplaceholder_get_diff_ip(amount, path_results):
    base_url = 'https://jsonplaceholder.typicode.com'
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        utils.change_ip()
        start_time = time.time()
        json_data = make_tor_request(f"{base_url}/posts/1", headers, config.proxies).json()
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{json_data}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/jsonplaceholder_get_results_diff_ip.txt")

def test_jsonplaceholder_get_same_ip(amount, path_results):
    base_url = 'https://jsonplaceholder.typicode.com'
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        start_time = time.time()
        json_data = make_tor_request(f"{base_url}/posts/1", headers, config.proxies).json()
        end_time = time.time()
        total_time = end_time - start_time
        additional_content = f"{json_data}\n"
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/jsonplaceholder_get_results_same_ip.txt")

def fetch_webpage_diff_ip(webpage, amount, path_results):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        utils.change_ip()
        
        start_time = time.time()
        response = make_tor_request(webpage, headers, config.proxies)
        end_time = time.time()
        
        total_time = end_time - start_time
        additional_content = f"{response.status_code}, {webpage}\n"
        
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/webpage_fetch_results_diff_ip.txt")

def fetch_webpage_same_ip(webpage, amount, path_results):
    for repeat in range(amount):
        headers = {'User-Agent': UserAgent().random}
        
        start_time = time.time()
        response = make_tor_request(webpage, headers, config.proxies)
        end_time = time.time()
        
        total_time = end_time - start_time
        additional_content = f"{response.status_code}, {webpage}\n"
        
        get_save_data_and_save(path_results, additional_content, headers, total_time, "/webpage_fetch_results_same_ip.txt")

def test_mongodb_find_diff_ip(amount, path_results):
    for _ in range(amount):
        utils.change_ip()

        client = utils.create_mongo_client()
        db = client[config.db_config['dbname']]
        collection = db[config.db_config['collection']]

        start_time = time.time()
        results = collection.find({"property_type": "house"})
        list(results)
        end_time = time.time()

        total_time = end_time - start_time
        additional_content = f"\n"
        get_save_data_and_save(path_results, additional_content, headers=None, total_time=total_time, filename="/mongodb_find_results_diff_ip.txt")

def test_mongodb_find_same_ip(amount, path_results):
    client = utils.create_mongo_client()
    db = client[config.db_config['dbname']]
    collection = db[config.db_config['collection']]

    for _ in range(amount):
        start_time = time.time()
        results = collection.find({"property_type": "house"})
        list(results)
        end_time = time.time()

        total_time = end_time - start_time
        additional_content = f"\n"
        get_save_data_and_save(path_results, additional_content, headers=None, total_time=total_time, filename="/mongodb_find_results_same_ip.txt")

def test_dns_resolution_diff_ip(hostname, amount, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        utils.change_ip()
        start_time = time.time()
        
        url = f"http://{hostname}"

        response = make_tor_request(url, headers, config.proxies)

        additional_content = "\n"
        end_time = time.time()
        total_time = end_time - start_time
        
        get_save_data_and_save(path_results, additional_content, headers=None, total_time=total_time, filename="/dns_resolution_results_diff_ip.txt")

def test_dns_resolution_same_ip(hostname, amount, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        start_time = time.time()
        
        url = f"http://{hostname}"

        response = make_tor_request(url, headers, config.proxies)

        additional_content = "\n"
        end_time = time.time()
        total_time = end_time - start_time
        
        get_save_data_and_save(path_results, additional_content, headers=None, total_time=total_time, filename="/dns_resolution_results_same_ip.txt")

def test_websocket_connection_diff_ip(url, amount, path_results):
    for _ in range(amount):
        utils.change_ip()
        start_time = time.time()
        
        try:
            ws = websocket.WebSocket()
            ws.connect(url, http_proxy_host="127.0.0.1", http_proxy_port=9050, proxy_type="socks5")

            end_time = time.time()
            total_time = end_time - start_time
            ws.close()
            
            additional_content = f"Connected to {url}\n"
            get_save_data_and_save(path_results, additional_content, headers=None, total_time=total_time, filename="/websocket_results_diff_ip.txt")
        
        except Exception as e:
            print(f"Error during WebSocket connection: {e}")
            total_time = None

def test_websocket_connection_same_ip(url, amount, path_results):
    for _ in range(amount):
        start_time = time.time()
        
        try:
            ws = websocket.WebSocket()
            ws.connect(url, http_proxy_host="127.0.0.1", http_proxy_port=9050, proxy_type="socks5")
            
            end_time = time.time()
            total_time = end_time - start_time
            ws.close()
            
            additional_content = f"Connected to {url}\n"
            get_save_data_and_save(path_results, additional_content, headers=None, total_time=total_time, filename="/websocket_results_same_ip.txt")
        
        except Exception as e:
            print(f"Error during WebSocket connection: {e}")
            total_time = None

def test_requests(webpage, amount, path_results):
    make_pings_diff_ip(webpage, amount, path_results)
    make_pings_same_ip(webpage, amount, path_results)

def test_images_download_time(webpage, amount, path_results, path_download):
    check_first_image_download_time_diff_ip(webpage, amount, path_results, path_download)
    check_first_image_download_time_same_ip(webpage, amount, path_results, path_download)

def test_download_file(webpage, amount, path_results, path_download):
    download_file_diff_ip(webpage, amount, path_results, path_download)
    download_file_same_ip(webpage, amount, path_results, path_download)

def test_json(amount, path_results):
    test_jsonplaceholder_get_diff_ip(amount, path_results)
    test_jsonplaceholder_get_same_ip(amount, path_results)

def test_webpage_fetch(webpage, amount, path_results):
    fetch_webpage_diff_ip(webpage, amount, path_results)
    fetch_webpage_same_ip(webpage, amount, path_results)

def test_mongodb_querry(amount, path_results):
    test_mongodb_find_diff_ip(amount, path_results)
    test_mongodb_find_same_ip(amount, path_results)

def test_dns_resolution(hostname, amount, path_results):
    test_dns_resolution_diff_ip(hostname, amount, path_results)
    test_dns_resolution_same_ip(hostname, amount, path_results)

def test_websocket_connection(url, amount, path_results):
    test_websocket_connection_diff_ip(url, amount, path_results)
    test_websocket_connection_same_ip(url, amount, path_results)

