# Lists comprehensions
def run():
    # Using for loop
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # Using lists comprehensions
    # list = ['element' for 'element' in 'iterable' if 'condition']
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)

    # List of multiples of 4, 6 and 9 from 1 to 99,999
    numbers = [i for i in range(1,100000) if i % 36 == 0]
    print(numbers)

if __name__ == '__main__':
    run()