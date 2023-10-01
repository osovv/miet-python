import itertools
def split_by_lambda(a, f):
    return [list(x[1]) for x in itertools.groupby(a, f) if not x[0]]