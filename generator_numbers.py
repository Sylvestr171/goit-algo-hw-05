import re
from typing import Generator, Callable

def generator_nambers(text: str) -> Generator[float]:
    '''
    Аналізує текст, ідентифікує всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор
    '''
    filter_num = re.finditer(r'\d+\.*\d*', text)
    for match in filter_num:
        yield float(match.group())

#     filter(r"^\s\d+,*\d*\s?$", text.split())

# def sum_profit(text: str, func: Callable):
#     '''
#     Використовуючи generator_numbers шляхом підсумовування чисел обчислює загальний прибуток
#     '''
#     ...


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

i=generator_nambers(text)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# filter_num = finditer(r'\d+\.*\d*', text)
# # for i in map(lambda x: int(x), filter_text):
# #     print (i)
# # print (type(filter_text[0]))
# # for i in text.split():
# #     if i==r"^\d+\.*\d*$":
# #         filter_text.append(i)
# print (filter_text)
# total_income = sum_profit(text, generator_numbers)

# print(f"Загальний дохід: {total_income}")

#^\s\d+,*\d*$