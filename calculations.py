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
    time_std_diff_ip = np.std(time_values_diff_ip)
    time_min_diff_ip = min(time_values_diff_ip)
    time_max_diff_ip = max(time_values_diff_ip)

    time_mean_same_ip = sum(time_values_same_ip) / len(time_values_same_ip)
    time_std_same_ip = np.std(time_values_same_ip)
    time_min_same_ip = min(time_values_same_ip)
    time_max_same_ip = max(time_values_same_ip)

    with open(f'statistics/statistics_{file_name}.txt', 'w') as fw:
        fw.write("Statystyki dla różnych adresów IP: \n")
        fw.write(f"Średnia czasu: {time_mean_diff_ip}\n")
        fw.write(f"Odchylenie standardowe czasu: {time_std_diff_ip}\n")
        fw.write(f"Minimalny czas: {time_min_diff_ip}\n")
        fw.write(f"Maksymalny czas: {time_max_diff_ip}\n")
        fw.write("\n")

        fw.write("Statystyki dla tego samego adresu IP: \n")
        fw.write(f"Średnia czasu: {time_mean_same_ip}\n")
        fw.write(f"Odchylenie standardowe czasu: {time_std_same_ip}\n")
        fw.write(f"Minimalny czas: {time_min_same_ip}\n")
        fw.write(f"Maksymalny czas: {time_max_same_ip}\n")
    fw.close()
