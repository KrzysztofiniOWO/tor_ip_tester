import functions
import calculations
import os 

def get_db_password(file_path):
    with open (file_path, 'r') as f:
        password = f.read().strip()
    f.close()
    return password

results_path = 'results'
downloads_path = 'downloads'
statistics_path = 'statistics'
test_data_path = '/test_data'

db_password = get_db_password('db_pass.txt')

db_config = {
    'uri': f'mongodb+srv://{db_password}@cluster0.x1x8qhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',  
    'dbname': 'inzynierka',
    'collection': 'sample_airbnb'
}
query = {"property_type": "house"}

if not os.path.exists("downloads"):
    os.makedirs("downloads")

if not os.path.exists("results"):
    os.makedirs("results")

if not os.path.exists("statistics"):
    os.makedirs("statistics")

repeats = int(input("How many requests you want to make?: "))

# functions.test_requests('https://www.wp.pl/', repeats, results_path)

# functions.test_images_download_time('https://store.steampowered.com/', repeats, results_path, downloads_path)

# functions.test_mongodb(repeats, results_path, db_config, query)

# functions.test_download_file("https://sample-videos.com/download-sample-text-file.php", repeats, results_path, downloads_path)

# functions.test_upload_file_ftp('eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp', repeats, f'{test_data_path}/sus.jpg', results_path)

# functions.test_json(repeats, results_path)

# functions.test_dns_resolution("example.com", repeats, results_path)

# functions.test_websocket("wss://echo.websocket.org", repeats, results_path)