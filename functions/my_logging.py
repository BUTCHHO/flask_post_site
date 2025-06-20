from os import path

from datetime import datetime

LOGS_FILE_LOCATION = path.abspath(path.join(path.dirname(__file__), '..', 'logs'))

def log(error, func):
    func_name = func.__name__
    time_logged = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file_path = path.join(LOGS_FILE_LOCATION, 'logs.txt')
    with open(log_file_path, 'a') as file:
        file.write(f"\n {func_name} | {error} | {time_logged} | ")
        print('!ERROR LOGGED!')

def write_logs(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        start_time = datetime.now()
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            exec_time = datetime.now() - start_time
            log_file_path = path.join(LOGS_FILE_LOCATION, 'logs.txt')
            with open(log_file_path, 'a') as logs_file:
                logs_file.write(f'{function_name} | {exec_time} | {datetime.now()}| {error} \n')
            print('!ERROR LOGGED!')
    return wrapper




