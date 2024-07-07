import functions
import calculations

results_path = '/home/krzysztof/tor_ip_tester/results'
downloads_path = '/home/krzysztof/tor_ip_tester/downloads'

db_config = {
    'uri': 'mongodb+srv://molakrzysztof:IFEIsvtxw0s34P7g@cluster0.x1x8qhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',  
    'dbname': 'inzynierka',
    'collection': 'sample_airbnb'
}
query = {"property_type": "house"}

repeats = int(input("How many requests you want to make?: "))

#functions.make_tor_requests_diff_ip('https://wp.pl', repeats, results_path)
#functions.make_tor_requests_same_ip('https://wp.pl', repeats, results_path)

functions.check_first_image_download_time_diff_ip('https://wp.pl', repeats, results_path, downloads_path)
functions.check_first_image_download_time_same_ip('https://wp.pl', repeats, results_path, downloads_path)

# calculations.mean_of_requests_time("results_diff_ip.txt")
# calculations.mean_of_requests_time("results_same_ip.txt")

#functions.test_mongodb_diff_ip(3, '/home/krzysztof/tor_ip_tester', db_config, query)
#functions.test_mongodb_same_ip(3, '/home/krzysztof/tor_ip_tester', db_config, query)

#functions.download_file_same_ip("https://sample-videos.com/download-sample-text-file.php", 5, '/home/krzysztof/tor_ip_tester')
#functions.download_file_diff_ip("https://sample-videos.com/download-sample-text-file.php", 5, '/home/krzysztof/tor_ip_tester')