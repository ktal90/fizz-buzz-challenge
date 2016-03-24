import unittest
import fizz_buzz_challenge


class TestFizzBuzz(unittest.TestCase):

    def test_div_by_3(self):
        assert 'Buzz' in fizz_buzz_challenge.get_fizz_buzz_value(3)
        assert 'Buzz' in fizz_buzz_challenge.get_fizz_buzz_value(9)

    def test_div_by_5(self):
    	assert 'Fizz' in fizz_buzz_challenge.get_fizz_buzz_value(5)
        assert 'Fizz' in fizz_buzz_challenge.get_fizz_buzz_value(10)

    def test_prime(self):
    	assert fizz_buzz_challenge.is_prime(2) is True
    	assert fizz_buzz_challenge.is_prime(7) is True

	def test_not_prime(self):
		assert fizz_buzz_challenge.is_prime(4) is False

    def test_fib(self):
        expected = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        assert fizz_buzz_challenge.generate_fib(10) == expected

if __name__ == '__main__':
	unittest.main()