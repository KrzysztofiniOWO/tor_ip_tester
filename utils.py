import config

import time
from stem.control import Controller
from stem import Signal
import requests
from pymongo import MongoClient
import ftplib
import websockets
import os

import config

def make_directories():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    if not os.path.exists("results"):
        os.makedirs("results")

    if not os.path.exists("statistics"):
        os.makedirs("statistics")

def change_ip():
    time.sleep(10)
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

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
    
def create_mongo_client():
    uri = f"{config.db_config['uri']}&proxyHost=127.0.0.1&proxyPort=9050"
    
    client = MongoClient(uri, socketTimeoutMS=5000, serverSelectionTimeoutMS=5000)
    return client
