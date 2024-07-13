import time
import requests
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
import ftplib

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

def make_tor_requests_diff_ip(webpage, amount, path):
    for _ in range(amount):
        headers = { 'User-Agent': UserAgent().random }
        change_ip()
        start_time = time.time()
        response = make_tor_request(webpage, headers, proxies)
        end_time = time.time()
        total_time = end_time - start_time
        my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
        result = f"{my_ip}, " + f"{total_time}, " + f"{response.status_code}" + f" {webpage}\n"
        result_file_name = f"{path}/ping_results_diff_ip.txt"
        save_results(result, result_file_name)

def make_tor_requests_same_ip(webpage, amount, path):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        start_time = time.time()
        response = make_tor_request(webpage, headers, proxies)
        end_time = time.time()
        total_time = end_time - start_time
        my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
        result = f"{my_ip}, " + f"{total_time}, " + f"{response.status_code}" + f" {webpage}\n"
        result_file_name = f"{path}/ping_results_same_ip.txt"
        save_results(result, result_file_name)

def check_first_image_download_time_diff_ip(webpage, amount, path_result, path_download):
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
            my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
            result = f"{my_ip}, " + f"{total_time}, " + f"{response.status_code}" + f" {webpage}\n"
            result_file_name = f"{path_result}/image_dl_results_diff_ip.txt"
            save_results(result, result_file_name)
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
            my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
            result = f"{my_ip}, " + f"{total_time}, " + f"{response.status_code}" + f" {webpage}\n"
            result_file_name = f"{path_results}/image_dl_results_same_ip.txt"
            save_results(result, result_file_name)
        else:
            print("Image could not be found")

def test_mongodb_diff_ip(amount, path, db_config, query):
    for _ in range(amount):
        change_ip()
        total_time = test_mongodb_query(db_config['uri'], db_config['dbname'], db_config['collection'], query)
        my_ip = requests.get("http://httpbin.org/ip", proxies=proxies).json()["origin"]
        result = f"{my_ip}, {total_time}\n"
        result_file_name = f"{path}/mongodb_results_diff_ip.txt"
        save_results(result, result_file_name)

def test_mongodb_same_ip(amount, path, db_config, query):
    for _ in range(amount):
        total_time = test_mongodb_query(db_config['uri'], db_config['dbname'], db_config['collection'], query)
        my_ip = requests.get("http://httpbin.org/ip", proxies=proxies).json()["origin"]
        result = f"{my_ip}, {total_time}\n"
        result_file_name = f"{path}/mongodb_results_same_ip.txt"
        save_results(result, result_file_name)

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
            end_time = time.time()
            download_time = end_time - start_time
            
            with open(f"{path_download}/{file_name}", 'wb') as f:
                for chunk in response_file.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            
            my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
            result = f"{my_ip}, " + f"{download_time}, " + f"{response_file.status_code}" + f" {file_url}\n"
            result_file_name = f"{path_results}/file_dl_results_diff_ip.txt"
            save_results(result, result_file_name)
            
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
            end_time = time.time()
            download_time = end_time - start_time
            
            with open(f"{path_download}/{file_name}", 'wb') as f:
                for chunk in response_file.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            
            my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
            result = f"{my_ip}, " + f"{download_time}, " + f"{response_file.status_code}" + f" {file_url}\n"
            result_file_name = f"{path_results}/file_dl_results_same_ip.txt"
            save_results(result, result_file_name)
            
        else:
            print("Download link not found")

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

def test_upload_file_ftp_diff_ip(server, username, password, amount, file_path, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        change_ip()
        upload_time = upload_file_ftp(server, username, password, file_path)
        if upload_time:
            my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
            result = f"IP Address: {my_ip}, Upload Time: {upload_time:.2f} seconds\n"
            name = f"{path_results}/ftp_upload_diff_ip.txt"
            save_results(result, name)
        else:
            print("Failed to upload file")

def test_upload_file_ftp_same_ip(server, username, password, amount, file_path, path_results):
    for _ in range(amount):
        headers = {'User-Agent': UserAgent().random}
        upload_time = upload_file_ftp(server, username, password, file_path)
        if upload_time:
            my_ip = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies).json()["origin"]
            result = f"IP Address: {my_ip}, Upload Time: {upload_time:.2f} seconds\n"
            name = f"{path_results}/ftp_upload_same_ip.txt"
            save_results(result, name)
        else:
            print("Failed to upload file")
        
def save_results(result, name):
    with open(name, 'a') as file:
        file.write(result)

def save_image(image_data, location):
    with open(location, 'wb') as f:
        f.write(image_data)