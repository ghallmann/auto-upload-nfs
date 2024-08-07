from datetime import datetime

def write_log(file_path, message):
    with open('logs.txt', 'a') as log_file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{current_time}, {file_path}, {message}\n")
