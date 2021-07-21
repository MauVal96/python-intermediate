# Handling Exceptions using try, raise and except
def divisors(num):
    try:
        if num < 1:
            raise ValueError("Number value must be greater than 0")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input("Enter a number: "))
        print(divisors(num))
        print("Program terminated")
    except ValueError:
        print("You must enter a number")


if __name__ == '__main__':
    run()