def prefill(n,v):
    if type(n) == str and n.isnumeric():
        n = int(n)
    if type(n) == int and n >= 0:
        return [v for i in range(n)]
    else:
        raise TypeError(f'{n} is invalid')