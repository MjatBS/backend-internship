def fibonacci(n):
    '''calculate Fibonacci series'''
    if n < 0:
        return []
    else:
        gen = fibonacci_gen()
        return [next(gen) for _ in range(n)]


def fibonacci_gen():
    '''Generate Fibonacci elements from the first position'''
    now = 0
    next_ = 1
    while True:
        yield now
        now, next_ = next_, now + next_


