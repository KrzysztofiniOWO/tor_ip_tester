def calculate_mean_time(file_path):
    time_values = []

    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) >= 2:
                try:
                    time_value = float(parts[1])
                    time_values.append(time_value)
                except ValueError:
                    continue

    f.close()
    if time_values:
        mean_time = sum(time_values) / len(time_values)
        with open(f'statistics/statistics_'+file_path, 'w') as output_file:
            output_file.write(f"Mean time: {mean_time}\n")
        print('kurwa')
        return mean_time
    else:
        return None
