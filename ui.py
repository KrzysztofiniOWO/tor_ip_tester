import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import functions
import calculations
import config

def start_tests(repeats_entry, test_vars, progress_bar):
    try:
        repeats = int(repeats_entry.get())

        selected_tests = [key for key, var in test_vars.items() if var.get()]
        total_tests = len(selected_tests)
        completed_tests = 0

        def update_progress():
            nonlocal completed_tests
            completed_tests += 1
            progress = (completed_tests / total_tests) * 100
            progress_bar['value'] = progress
            root.update_idletasks()

        if test_vars['requests'].get():
            functions.test_requests(*config.test_requests_params, repeats, config.results_path)
            calculations.calculate_times("ping_results_")
            update_progress()
            
        if test_vars['images_download_time'].get():
            functions.test_images_download_time(*config.test_images_download_time_params, repeats, config.results_path, config.downloads_path)
            calculations.calculate_times("image_dl_results_")
            update_progress()
        
        if test_vars['mongodb'].get():
            functions.test_mongodb(repeats, config.results_path, config.db_config, config.db_query)
            calculations.calculate_times("mongodb_results_")
            update_progress()

        if test_vars['download_file'].get():
            functions.test_download_file(*config.test_download_file_params, repeats, config.results_path, config.downloads_path)
            calculations.calculate_times("file_dl_results_")
            update_progress()

        if test_vars['upload_file_ftp'].get():
            functions.test_upload_file_ftp(*config.test_upload_file_ftp_params, repeats, f'{config.test_data_path}/sus.jpg', config.results_path)
            calculations.calculate_times("ftp_upload_results_")
            update_progress()

        if test_vars['json'].get():
            functions.test_json(repeats, config.results_path)
            calculations.calculate_times("jsonplaceholder_get_results_")
            update_progress()

        if test_vars['dns_resolution'].get():
            functions.test_dns_resolution(*config.test_dns_resolution_params, repeats, config.results_path)
            calculations.calculate_times("dns_resolution_name_results")
            update_progress()

        if test_vars['websocket'].get():
            functions.test_websocket(config.test_websocket_params, repeats, config.results_path)
            calculations.calculate_times("websocket_results_")
            update_progress()

        if test_vars['webpage_fetch'].get():
            functions.test_webpage_fetch(*config.test_webpage_fetch_params, repeats, config.results_path)
            calculations.calculate_times("webpage_fetch_results_")
            update_progress()

        messagebox.showinfo("Success", "Tests completed!")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for repeats.")

def create_ui():
    global root

    root = tk.Tk()
    root.title("Test Program")
    root.geometry("400x320")
    root.configure(bg="#2d2d30")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Helvetica", 10, "bold"), foreground="#ffffff", background="#1e90ff", padding=6, borderwidth=0)
    style.map("TButton", background=[("active", "#1c86ee")])
    style.configure("TLabel", font=("Helvetica", 10), foreground="#ffffff", background="#2d2d30")
    style.configure("TCheckbutton", font=("Helvetica", 10), foreground="#ffffff", background="#2d2d30")
    style.configure("TEntry", font=("Helvetica", 10), fieldbackground="#3b3b3b", foreground="#ffffff", borderwidth=2)
    style.configure("TProgressbar", thickness=20, troughcolor='#353535', background='#00bfff', relief="flat")

    ttk.Label(root, text="Number of Repeats:").grid(column=0, row=0, padx=8, pady=8, sticky=tk.W)
    repeats_entry = ttk.Entry(root, style="TEntry")
    repeats_entry.grid(column=1, row=0, padx=8, pady=8)

    test_vars = {
        'requests': tk.BooleanVar(),
        'images_download_time': tk.BooleanVar(),
        'mongodb': tk.BooleanVar(),
        'download_file': tk.BooleanVar(),
        'upload_file_ftp': tk.BooleanVar(),
        'json': tk.BooleanVar(),
        'dns_resolution': tk.BooleanVar(),
        'websocket': tk.BooleanVar(),
        'webpage_fetch': tk.BooleanVar()
    }

    ttk.Checkbutton(root, text="Test Requests", variable=test_vars['requests']).grid(column=0, row=1, sticky=tk.W)
    ttk.Checkbutton(root, text="Test Image Download Time", variable=test_vars['images_download_time']).grid(column=0, row=2, sticky=tk.W)
    ttk.Checkbutton(root, text="Test MongoDB", variable=test_vars['mongodb']).grid(column=0, row=3, sticky=tk.W)
    ttk.Checkbutton(root, text="Test Download File", variable=test_vars['download_file']).grid(column=0, row=4, sticky=tk.W)
    ttk.Checkbutton(root, text="Test Upload File via FTP", variable=test_vars['upload_file_ftp']).grid(column=0, row=5, sticky=tk.W)
    ttk.Checkbutton(root, text="Test JSON", variable=test_vars['json']).grid(column=0, row=6, sticky=tk.W)
    ttk.Checkbutton(root, text="Test DNS Resolution", variable=test_vars['dns_resolution']).grid(column=0, row=7, sticky=tk.W)
    ttk.Checkbutton(root, text="Test WebSocket", variable=test_vars['websocket']).grid(column=0, row=8, sticky=tk.W)
    ttk.Checkbutton(root, text="Test Webpage Fetch", variable=test_vars['webpage_fetch']).grid(column=0, row=9, sticky=tk.W)

    progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=260, style="TProgressbar")
    progress_bar.grid(column=0, row=10, columnspan=2, pady=12)

    start_button = ttk.Button(root, text="Start", command=lambda: start_tests(repeats_entry, test_vars, progress_bar), style="TButton")
    start_button.grid(column=0, row=11, columnspan=2, pady=10)

    root.mainloop()
