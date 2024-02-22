import functions
import calculations

repeats = int(input("How many requests you want to make?: "))

functions.make_tor_requests_diff_ip(repeats)
functions.make_tor_requests_same_ip(repeats)

calculations.mean_of_requests_time(repeats)
