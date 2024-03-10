import statistics

def mean_of_requests_time(file_name):
    with open(file_name, 'r') as file:
        results = file.readlines()
        times = []
        for result in results:
            split_result = result.split(",")
            times.append(round(float(split_result[1]), 3))
        mean_ip_time = round(statistics.mean(times), 3)
        print(mean_ip_time)
