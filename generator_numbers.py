import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float]:
    '''
    Аналізує текст, ідентифікує всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор
    '''
    filter_num = re.finditer(r'\s\d+\.*\d*\s', text)
    for match in filter_num:
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    '''
    Використовуючи generator_numbers шляхом підсумовування чисел обчислює загальний прибуток
    '''
    total_profit=0.0
    for value_profit in func(text):
        total_profit += value_profit 
    return total_profit


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")