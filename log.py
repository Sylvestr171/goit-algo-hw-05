from sys import argv, exit
from pathlib import Path
from datetime import date, time
from collections import defaultdict

#декоратор для обробки помилок
def FileNotFoundError_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            return "'FileNotFoundError' Please input correct path"
    return inner

#функція завантаження логу з файлу
@FileNotFoundError_error
def load_logs(file_path: str) -> list[dict]:
    log_dict_list = []
    with open(file_path, "r", encoding="utf-8") as file:
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
    return list(filter(lambda x: x['level'] == level, logs))


#функція підрахунку кількості повідомлень за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    count_dict = defaultdict(int)
    for line in logs:
        count_dict[line['level']]+=1
    return count_dict


#функція для виводу статистики логування
def display_log_counts(counts: dict):
    print('Рівень логування', 'Кількість', sep='\t|    ')
    print('------------------------|------------------')
    for ithem in counts.keys():
         print (ithem, counts.get(ithem), sep='\t\t\t|\t') 



# log_dict_list = load_logs('log.txt')
# for i in log_dict_list:
#     print (i)

# filter_mesage=filter_logs_by_level(log_dict_list, 'INFO')
# # for k in filter_mesage:
# #     print (type(k))
#print(count_logs_by_level(log_dict_list))
# display_log_counts(count_logs_by_level(log_dict_list))



if __name__ == '__main__':

    if len(argv) == 2:
        file_path = str(argv[1])
        log_dict_list = load_logs(file_path)
        display_log_counts(count_logs_by_level(log_dict_list))
    elif len(argv) == 3:
        file_path = argv[1]
        level_param = argv[2].upper()
        log_dict_list = load_logs(file_path)
        count_dict=count_logs_by_level(log_dict_list)
        display_log_counts(count_dict)
        if level_param in count_dict.keys():
            filter_mesage=filter_logs_by_level(log_dict_list, level_param)
            print (f'\nДеталі логів для рівня "{level_param}":')
            for ithem in filter_mesage:
                print (ithem['date'].isoformat(), ithem['time'].isoformat(), '-', ithem['info'], sep=' ')
        else:
            print (f'Incorrect level parameter {level_param}')
    elif len(argv) == 1:
        print('Please insert path to file')
        exit()
    else:
        print('More parameters than expected')
        exit()
    
    # log_dict_list = load_logs(file_path)
    # filter_mesage=filter_logs_by_level(log_dict_list, level_param)
    # # for k in filter_mesage:
    # #     print (type(k))
    # print(count_logs_by_level(log_dict_list))
    # display_log_counts(count_logs_by_level(log_dict_list))
