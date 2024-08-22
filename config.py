import utils

db_password = utils.get_db_password('db_pass.txt')

db_config = {
    'uri': f'mongodb+srv://{db_password}@cluster0.x1x8qhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',  
    'dbname': 'inzynierka',
    'collection': 'sample_airbnb'
}

db_query = {"property_type": "house"}

results_path = 'results'
downloads_path = 'downloads'
statistics_path = 'statistics'
test_data_path = 'test_data'

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

test_requests_params = ['https://store.steampowered.com/']
test_images_download_time_params = ['https://store.steampowered.com/']
test_download_file_params = ["https://sample-videos.com/download-sample-text-file.php"]
test_upload_file_ftp_params = ['eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp']
test_dns_resolution_params = ["example.com"]
test_websocket_params = ["wss://echo.websocket.org"]
test_webpage_fetch_params = ["https://psiaki.fandom.com/pl/wiki/Pies_domowy"]