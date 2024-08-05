import functions
import calculations
import os 

def get_db_password(file_path):
    with open (file_path, 'r') as f:
        password = f.read().strip()
    f.close()
    return password

results_path = '/home/krzysztof/tor_ip_tester/results'
downloads_path = '/home/krzysztof/tor_ip_tester/downloads'
test_data_path = '/home/krzysztof/tor_ip_tester/test_data'

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

# functions.make_requests_diff_ip('https://wp.pl', repeats, results_path)
# functions.make_requests_same_ip('https://wp.pl', repeats, results_path)

# functions.check_first_image_download_time_diff_ip('https://wp.pl', repeats, results_path, downloads_path)
# functions.check_first_image_download_time_same_ip('https://wp.pl', repeats, results_path, downloads_path)

# functions.test_mongodb_diff_ip(repeats, results_path, db_config, query)
# functions.test_mongodb_same_ip(repeats, results_path, db_config, query)

# functions.download_file_diff_ip("https://sample-videos.com/download-sample-text-file.php", repeats, results_path, downloads_path)
# functions.download_file_same_ip("https://sample-videos.com/download-sample-text-file.php", repeats, results_path, downloads_path)

# functions.test_upload_file_ftp_diff_ip('eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp', repeats, f'{test_data_path}/sus.jpg', results_path)
# functions.test_upload_file_ftp_same_ip('eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp', repeats, f'{test_data_path}/sus.jpg', results_path)

# functions.test_jsonplaceholder_get_diff_ip(repeats, results_path)
# functions.test_jsonplaceholder_get_same_ip(repeats, results_path)

# functions.test_dns_resolution_diff_ip("example.com", repeats, results_path)
# functions.test_dns_resolution_same_ip("example.com", repeats, results_path)

# functions.test_websocket_diff_ip("wss://echo.websocket.org", repeats, results_path)
# functions.test_websocket_same_ip("wss://echo.websocket.org", repeats, results_path)