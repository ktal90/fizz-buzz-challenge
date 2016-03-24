import math


def is_prime(val):
    """ Returns whether given number is prime or not using the basic
    approach of checking if any numbers up to the square root of val
    is divisible by the value."""
    if val == 2:
        return True
    if val % 2 == 0:
        return False  # Checking this makes this much more efficient
    for i in xrange(2, int(math.sqrt(val)) + 1):
        if val % i == 0:
            return False
    return True


def get_fizz_buzz_value(val):
    """Returns the value(s) based on the the FizzBuzz rules as an array:
    'Buzz' when F(n) is divisible by 3
    'Fizz' when F(n) is divisible by 5
    'BuzzFizz' when F(n) is prime
    the value F(n) otherwise
    """
    fizz_buzz = []
    if val % 3 == 0:
        fizz_buzz.append('Buzz')
    if val % 5 == 0:
        fizz_buzz.append('Fizz')
    if is_prime(val):
        fizz_buzz.append('FizzBuzz')
    return fizz_buzz


def generate_fib(n):
    """This method generates the first n Fibonacci numbers and retuns
    them as an array. In addition, this function calls the FizzBuzz method for
    each Fibonacci number and prints the return value(s).
    """
    fib_array = [0]
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
        fib_array.append(a)
        print get_fizz_buzz_value(a)
    return fib_array

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1:
        print 'Please provide an n value for this FizzBuzz'
    n = int(sys.argv[1])  # The first argument passed in
    print generate_fib(n)
