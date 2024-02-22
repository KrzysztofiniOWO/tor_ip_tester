import statistics

def mean_of_requests_time(repeats):
    with open("request_results.txt", 'r') as file:
        half = int(repeats/2)
        results = file.readlines()
        mean_diff_ip = statistics.mean(results[:half])
        mean_same_ip = statistics.mean(results[half:])
        print(f"Mean diff ip: {mean_diff_ip}")
        print(f"Mean same ip: {mean_same_ip}")
