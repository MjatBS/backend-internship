def Xbonacci(signature, n):
    '''calculate Xbonacci series'''
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
        sum = 0
        for i in range(len(base) - 1):
            sum += base[i]
            base[i] = base[i+1]
        base[-1] += sum
        now = base[-1]
        yield now
