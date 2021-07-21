# Dictionary comprehensions
from math import sqrt

def run():
    # Using for loop
    # my_dict = {} 
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # Using Dictionary comprehensions
    # dict = {'key': 'value' for 'value' in 'iterable' if 'condition'}
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict)

    numbers = {i: sqrt(i) for i in range(1, 1001)}
    print(numbers)

    

if __name__ == '__main__':
    run()
