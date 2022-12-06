import collections


def flatten(*args):
    out = []
    for arg in args:
        if isinstance(arg, collections.abc.Iterable) and not isinstance(arg, str):
            out.extend(arg)
        else:
            out.append(arg)
    return out


def dictfilter(mapping, func):
    """
    Filters out values from a dictionary using a callback 
    function
    """
    return {k: v for k, v in mapping.items() if func(k, v)}

