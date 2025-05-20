# import re
# from typing import Generator, Callable

def generator_nambers(text: str) -> Generator[float]:
    '''
    Аналізує текст, ідентифікує всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор
    '''
    # for i in text.split():
    #     if i == r"^\s\d+,*\d*\s?$":
    #         yield float(i)

    filter(r"^\s\d+,*\d*\s?$", text.split())

# def sum_profit(text: str, func: Callable):
#     '''
#     Використовуючи generator_numbers шляхом підсумовування чисел обчислює загальний прибуток
#     '''
#     ...


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print (filter(i==r"^\s\d+,*\d*\s?$", text.split()))
# total_income = sum_profit(text, generator_numbers)

# print(f"Загальний дохід: {total_income}")

#^\s\d+,*\d*$