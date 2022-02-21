import collections


def flatten(*args):
    out = []
    for arg in args:
        if isinstance(arg, collections.abc.Iterable) and not isinstance(arg, str):
            out.extend(arg)
        else:
            out.append(arg)
    return out
