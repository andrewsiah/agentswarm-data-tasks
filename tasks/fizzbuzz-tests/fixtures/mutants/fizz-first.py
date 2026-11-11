def fizzbuzz(n):
    if type(n) is not int:
        raise TypeError('exact integer required')
    if n < 1:
        raise ValueError('n must be at least 1')
    if n % 3 == 0:
        return 'Fizz'
    if n % 15 == 0:
        return 'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)
