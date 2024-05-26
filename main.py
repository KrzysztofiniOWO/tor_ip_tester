import functions
import calculations

db_config = {
    'uri': 'mongodb+srv://molakrzysztof:<pass>@cluster0.x1x8qhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',  
    'dbname': 'inzynierka',
    'collection': 'sample_airbnb'
}
query = {"property_type": "house"}

#repeats = int(input("How many requests you want to make?: "))

# functions.make_tor_requests_diff_ip(repeats)
# functions.make_tor_requests_same_ip(repeats)

# img_load_time = functions.check_first_image_load_time_diff_ip(repeats)
# img_load_time = functions.check_first_image_load_time_same_ip(repeats)

# calculations.mean_of_requests_time("results_diff_ip.txt")
# calculations.mean_of_requests_time("results_same_ip.txt")

functions.test_mongodb_diff_ip(3, '/home/krzysztof/tor_ip_tester', db_config, query)
functions.test_mongodb_same_ip(3, '/home/krzysztof/tor_ip_tester', db_config, query)
