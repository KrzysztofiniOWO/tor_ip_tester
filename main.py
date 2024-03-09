import functions
import calculations

repeats = int(input("How many requests you want to make?: "))

functions.make_tor_requests_diff_ip(repeats)
functions.make_tor_requests_same_ip(repeats)

img_load_time = functions.check_first_image_load_time_diff_ip(repeats)
if img_load_time is not None:
    print(f"Download time for first image with diff ip is {img_load_time}")

img_load_time = functions.check_first_image_load_time_same_ip(repeats)
if img_load_time is not None:
    print(f"Download time for first image with diff ip is {img_load_time}")


calculations.mean_of_requests_time(repeats)
