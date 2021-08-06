def tribonacci(signature, n):
    '''calculate Tribonacci series'''
    if n < 0:
        return []
    else:
        gen = anybonacci_gen(signature)
        return [next(gen) for _ in range(n)]
    

def anybonacci_gen(signature):
    '''Generate Anybonacci elements from the first position
    Anybonacci sequence will created with any BASE [a, b, c, ..]
    Example:
        Fibonacci sequence have base [x, y]
        Tribonacci sequence have base [x, y, z] 
    '''
    base = signature[:]
    for now in base:
        yield now
    while True:
        base = base[1], base[2], base[0] + base[1] + base[2]
        now = base[2]
        yield now
