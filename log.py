from sys import argv
from pathlib import Path
from datetime import date, time
# import re


#функція завантаження логу з файлу
def load_logs(file_path: str) -> list:
    carrent_dir = Path(__file__).parent
    log_dict_list = []
    with open(carrent_dir / "log.txt", "r", encoding="utf-8") as file:
            for ithem in file.readlines():
                i=parse_log_line(ithem)
                log_dict_list.append(i)
            return log_dict_list

# функція парсингу рядків логу
def parse_log_line(line: str) -> dict:
    log_date=date.fromisoformat(line[0].split()[0])
    log_time=time.fromisoformat(line[0].split()[1])
    log_level=line[0].split()[2]
    log_message=' '.join(line[0].split()[3:])
    log_dict={'date':log_date, 'time':log_time, 'level': log_level, 'info':log_message}
    return log_dict

#функція фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    ...

#функція підрахунку кількості повідомлень за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    ...

#функція підрахунку кількості повідомлень за рівнем логування
def display_log_counts(counts: dict):
    ...

#декоратор для обробки помилок
def FileNotFoundError_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            return "How can I help you?"
    return inner

print (load_logs("log.txt"))
# log_line=['2024-01-22 08:30:01 INFO User logged in successfully.\n', '2024-01-22 08:45:23 DEBUG Attempting to connect to the database.\n', '2024-01-22 09:00:45 ERROR Database connection failed.\n', '2024-01-22 09:15:10 INFO Data export completed.\n', '2024-01-22 10:30:55 WARNING Disk usage above 80%.\n', '2024-01-22 11:05:00 DEBUG Starting data backup process.\n', '2024-01-22 11:30:15 ERROR Backup process failed.\n', '2024-01-22 12:00:00 INFO User logged out.\n', '2024-01-22 12:45:05 DEBUG Checking system health.\n', '2024-01-22 13:30:30 INFO Scheduled maintenance.\n']
# print(parse_log_line(log_line[0]))
