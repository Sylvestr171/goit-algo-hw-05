from sys import argv
from pathlib import Path
from datetime import date, time
# import re


#функція завантаження логу з файлу
def load_logs(file_path: str) -> list[dict]:
    carrent_dir = Path(__file__).parent
    log_dict_list = []
    with open(carrent_dir/file_path, "r", encoding="utf-8") as file:
            for ithem in file.readlines():
                log_dict_list.append(parse_log_line(ithem))
            return log_dict_list

# функція парсингу рядків логу
def parse_log_line(line: str) -> dict[str, date | time | str]:
    log_date=date.fromisoformat(line.split()[0])
    log_time=time.fromisoformat(line.split()[1])
    log_level=line.split()[2]
    log_message=' '.join(line.split()[3:])
    # log_dict={'date':log_date, 'time':log_time, 'level': log_level, 'message':log_message}
    return {
        'date':log_date, 
        'time':log_time, 
        'level': log_level, 
        'info':log_message
        }

#функція фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return filter(lambda x: x['level'] == level, logs)


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

log_dict_list = load_logs('log.txt')
for i in log_dict_list:
    print (i)

filter_mesage=filter_logs_by_level(log_dict_list, 'INFO')
for k in filter_mesage:
    print (k)