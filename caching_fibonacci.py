from collections import defaultdict
from typing import Callable, Dict

def caching_fibonacci() -> Callable:
    caching_dictionary = defaultdict(int)
    caching_dictionary = {0:0,1:1}
    print(caching_dictionary)
    print(caching_dictionary[0])
    print(caching_dictionary[1])
    def fibonachi(number:int) -> int:
        if number < 0:
            number = 0
        if number in caching_dictionary:
            return caching_dictionary[number]
        else:
            caching_dictionary[number] = fibonachi(number-1) + fibonachi(number-2)
            return caching_dictionary[number]
    return fibonachi

i=caching_fibonacci()


print([i(n) for n in range(500)])
