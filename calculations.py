import numpy as np

def calculate_times(file_name):
    file_path = f"results/{file_name}"

    time_values = []

    with open(file_path, 'r') as fr:
        for line in fr:
            parts = line.strip().split(', ')
            time_value = float(parts[1].rstrip(','))
            time_values.append(time_value)
    fr.close()

    time_mean = sum(time_values) / len(time_values)
    time_median = np.median(time_values)
    time_min = min(time_values)
    time_max = max(time_values)

    with open(f'statistics/statistics_{file_name}', 'w')as fw:
        fw.write(f"Mean of times: {time_mean}\n")
        fw.write(f"Median of times: {time_median}\n")
        fw.write(f"Min of times: {time_min}\n")
        fw.write(f"Max of times: {time_max}\n")
    fw.close()

