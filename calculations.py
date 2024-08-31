import numpy as np

def calculate_times(file_name):
    file_path_diff_ip = f"results/{file_name}diff_ip.txt"
    file_path_same_ip = f"results/{file_name}same_ip.txt"

    time_values_diff_ip = []
    time_values_same_ip = []

    with open(file_path_diff_ip, 'r') as fdr:
        for line in fdr:
            parts = line.strip().split(', ')
            time_value = float(parts[1].rstrip(','))
            time_values_diff_ip.append(time_value)
    fdr.close()

    with open(file_path_same_ip, 'r') as fsr:
        for line in fsr:
            parts = line.strip().split(', ')
            time_value = float(parts[1].rstrip(','))
            time_values_same_ip.append(time_value)
    fsr.close()

    time_mean_diff_ip = sum(time_values_diff_ip) / len(time_values_diff_ip)
    time_median_diff_ip = np.median(time_values_diff_ip)
    time_min_diff_ip = min(time_values_diff_ip)
    time_max_diff_ip = max(time_values_diff_ip)

    time_mean_same_ip = sum(time_values_same_ip) / len(time_values_same_ip)
    time_median_same_ip = np.median(time_values_same_ip)
    time_min_same_ip = min(time_values_same_ip)
    time_max_same_ip = max(time_values_same_ip)

    with open(f'statistics/statistics_{file_name}.txt', 'w')as fw:
        fw.write("Statictics for difefrent ip addresses: \n")
        fw.write(f"Mean of times: {time_mean_diff_ip}\n")
        fw.write(f"Median of times: {time_median_diff_ip}\n")
        fw.write(f"Min of times: {time_min_diff_ip}\n")
        fw.write(f"Max of times: {time_max_diff_ip}\n")
        fw.write("\n")

        fw.write("Statictics for same ip addresses: \n")
        fw.write(f"Mean of times: {time_mean_same_ip}\n")
        fw.write(f"Median of times: {time_median_same_ip}\n")
        fw.write(f"Min of times: {time_min_same_ip}\n")
        fw.write(f"Max of times: {time_max_same_ip}\n")
    fw.close()

