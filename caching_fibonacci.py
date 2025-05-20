from collections import defaultdict
from typing import Callable

# The function for cashing the calculating values of Fibonachi numbers
def caching_fibonacci() -> Callable:
    '''
    The function for cashing the calculating values 
    of Fibonachi numbers to the dict {key=number of Fibonachi number, value=value of Fibonachi number}
    
    return: function
    
    '''
    caching_dictionary = defaultdict(int)
    caching_dictionary = {0:0,1:1}
    # The function for calculating Fibonachi number
    def fibonachi(number:int) -> int:
        '''
        The function of calculating Fibonachi number
        if it not in cashing dictionary
        
        input: int
        return: int
        
        '''
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
