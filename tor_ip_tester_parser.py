import functions
import calculations
import argparse
import os

def run_tests(webpage, amount, path):
    functions.make_tor_requests_diff_ip(webpage, amount, path)
    functions.make_tor_requests_same_ip(webpage, amount, path)

    _ = functions.check_first_image_load_time_diff_ip(webpage, amount, path)
    _ = functions.check_first_image_load_time_same_ip(webpage, amount, path)

    calculations.mean_of_requests_time(f"{path}/results_diff_ip.txt")
    calculations.mean_of_requests_time(f"{path}/results_same_ip.txt")

def main():
    parser = argparse.ArgumentParser(description="Tor IP tester")
    parser.add_argument("-w", "--webpage", type=str, help="Address of webpage that will be tested")
    parser.add_argument("-a", "--amount", type=int, default=5, help="How many requests should be used")
    parser.add_argument("-p", "--path", type=str, default="results", help="Path to save the results")

    args = parser.parse_args()

    if not args.webpage:
        parser.error("Specify the page you want to test with --address")

    if not os.path.exists(args.path):
        os.makedirs(args.path)

    if not os.path.exists("results"):
        os.makedirs("results")

    run_tests(args.webpage, args.amount, args.path)
    print(f"Succesfully ran tests for {args.webpage}")

if __name__ == "__main__":
    main()