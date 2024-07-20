import functions
import calculations

results_path = '/home/krzysztof/tor_ip_tester/results'
downloads_path = '/home/krzysztof/tor_ip_tester/downloads'

db_config = {
    'uri': 'mongodb+srv://<pass>@cluster0.x1x8qhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',  
    'dbname': 'inzynierka',
    'collection': 'sample_airbnb'
}
query = {"property_type": "house"}

repeats = int(input("How many requests you want to make?: "))

functions.make_tor_requests_diff_ip('https://wp.pl', repeats, results_path)
functions.make_tor_requests_same_ip('https://wp.pl', repeats, results_path)

# functions.check_first_image_download_time_diff_ip('https://wp.pl', repeats, results_path, downloads_path)
# functions.check_first_image_download_time_same_ip('https://wp.pl', repeats, results_path, downloads_path)

# functions.test_mongodb_diff_ip(repeats, results_path, db_config, query)
# functions.test_mongodb_same_ip(repeats, results_path, db_config, query)

# functions.download_file_diff_ip("https://sample-videos.com/download-sample-text-file.php", repeats, results_path, downloads_path)
# functions.download_file_same_ip("https://sample-videos.com/download-sample-text-file.php", repeats, results_path, downloads_path)

# functions.test_upload_file_ftp_diff_ip('eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp', repeats, f'{downloads_path}/img_diff_ip_0.jpg', results_path)
# functions.test_upload_file_ftp_same_ip('eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp', repeats, f'{downloads_path}/img_diff_ip_0.jpg', results_path)

# functions.test_jsonplaceholder_get_diff_ip(repeats, results_path)
# functions.test_jsonplaceholder_get_same_ip(repeats, results_path)

functions.test_dns_resolution_diff_ip("example.com", repeats, results_path)
functions.test_dns_resolution_same_ip("example.com", repeats, results_path)

functions.test_websocket_diff_ip("wss://echo.websocket.org", repeats, results_path)
functions.test_websocket_same_ip("wss://echo.websocket.org", repeats, results_path)