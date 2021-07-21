# Handling errors using Assert Statements 
def divisors(num):
    assert num > 0, "Number value must be greater than 0"
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Enter a number: ")
    assert num.isnumeric(), "You must enter a number"  
    print(divisors(int(num)))
    print("Program terminated")

if __name__ == '__main__':
    run()