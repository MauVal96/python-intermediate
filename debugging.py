# Debugging code using VS Code
def divisors(num):
    divisors = []

    # Set wrong value in if condition i == 1
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    num = int(input("Enter a number: "))
    print(divisors(num))
    print("Program terminated")


if __name__ == '__main__':
    run()