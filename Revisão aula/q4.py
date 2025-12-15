def prange(start, stop, step):
    if start >= stop:
        return []
    
    return [start] + prange(start + step, stop, step)


print(prange(1, 9, 2))