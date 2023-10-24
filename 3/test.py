def descending_order(num):
    return sum([ x * (10**i) for i, x in enumerate(sorted(list(map(int, str(num)))))])

