import functions
import calculations

repeats = int(input("How many requests you want to make?: "))

functions.make_tor_requests_diff_ip(repeats)
functions.make_tor_requests_same_ip(repeats)

img_load_time = functions.check_first_image_load_time_diff_ip(repeats)
img_load_time = functions.check_first_image_load_time_same_ip(repeats)

calculations.mean_of_requests_time("results_diff_ip.txt")
calculations.mean_of_requests_time("results_same_ip.txt")
