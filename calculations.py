import statistics

def mean_of_requests_time(repeats):
    with open("request_results.txt", 'r') as file:
        half = int(repeats/2)
        results = file.readlines()
        times = []
        for result in results:
            split_result = result.split(",")
            times.append(round(float(split_result[1]), 3))
        mean_diff_ip = round(statistics.mean(times[:half]), 3)
        mean_same_ip = round(statistics.mean(times[half:]), 3)
        print(mean_diff_ip)
        print(mean_same_ip)
        print(f"Mean diff ip: {mean_diff_ip}")
        print(f"Mean same ip: {mean_same_ip}")
