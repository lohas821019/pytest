def add(x, y):
    if x is None or y is None:
        raise ValueError('Invalid input')
    z = x + y
    return z
