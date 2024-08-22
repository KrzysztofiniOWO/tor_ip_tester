import functions
import calculations
import utils
import config

db_config = config.db_config
query = config.db_query

utils.make_directories()

repeats = int(input("How many requests you want to make?: "))

#functions.test_requests('https://store.steampowered.com/', repeats, config.results_path)

#functions.test_images_download_time('https://store.steampowered.com/', repeats, config.results_path, config.downloads_path)

functions.test_mongodb(repeats, config.results_path, db_config, query)

#functions.test_download_file("https://sample-videos.com/download-sample-text-file.php", repeats, config.results_path, config.downloads_path)

#functions.test_upload_file_ftp('eu-west-1.sftpcloud.io', 'f831873852d84bb6b0c82e0f6549fd1b', 'vzy3qOglaqIZsmhzFrHtjAhIUevaKGDp', repeats, f'{config.test_data_path}/sus.jpg', config.results_path)

#functions.test_json(repeats, config.results_path)

#functions.test_dns_resolution("example.com", repeats, config.results_path)

#functions.test_websocket("wss://echo.websocket.org", repeats, config.results_path)