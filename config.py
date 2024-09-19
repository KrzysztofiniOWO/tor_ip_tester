def get_db_password(file_path):
    with open (file_path, 'r') as f:
        password = f.read().strip()
    f.close()
    return password

db_password = get_db_password('db_pass.txt')

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
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

test_requests_params = ['https://store.steampowered.com/']
test_images_download_time_params = ['https://store.steampowered.com/']
test_download_file_params = ["https://sample-videos.com/download-sample-text-file.php"]
test_upload_file_ftp_params = ['eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp']
test_webpage_fetch_params = ["https://psiaki.fandom.com/pl/wiki/Pies_domowy"]
test_post_form_params = ["http://httpbin.org/forms/post"]
test_dns_params = ["google.com"]