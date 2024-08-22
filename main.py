import functions
import calculations
import utils
import config

utils.make_directories()

repeats = int(input("How many requests you want to make?: "))

# functions.test_requests(*config.test_requests_params, repeats, config.results_path)

# functions.test_images_download_time(*config.test_images_download_time_params, repeats, config.results_path, config.downloads_path)

# functions.test_mongodb(repeats, config.results_path, config.db_config, config.db_query)

# functions.test_download_file(*config.test_download_file_params, repeats, config.results_path, config.downloads_path)

# functions.test_upload_file_ftp(*config.test_upload_file_ftp_params, repeats, f'{config.test_data_path}/sus.jpg', config.results_path)

# functions.test_json(repeats, config.results_path)

# functions.test_dns_resolution(*config.test_dns_resolution_params, repeats, config.results_path)

# functions.test_websocket(config.test_websocket_params, repeats, config.results_path)

functions.test_webpage_fetch(*config.test_webpage_fetch_params, repeats, config.results_path)