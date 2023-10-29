import collections


def flatten(*args) -> list:
    """
    Flatten a list of iterables (other than strings) into a
    flattened list

    Parameters
    ----------
    args : iterable
        iterable

    Returns
    -------
    list
    """
    out = []
    for arg in args:
        if isinstance(arg, collections.abc.Iterable) and not isinstance(arg, str):
            out.extend(arg)
        else:
            out.append(arg)
    return out


def dictfilter(mapping: dict, func: callable) -> dict:
    """
    Filters out values from a dictionary using a callback
    function

    Parameters
    ----------
    mapping : dict
        dict to filter
    func : callable
        function that accepts a key and value and returns a boolean
        value

    Returns
    -------
    dict
    """
    return {k: v for k, v in mapping.items() if func(k, v)}


def alias(argname: str, *aliases):
    """
    Rename aliased keyword arguments by its true argument name

    Parameters
    ----------
    argname : str
        true name of argument
    aliases : tuple[str]
        argument aliases

    Returns
    -------
    decorator : callable

    Note
    ----
    If multiple values are provided for a same argument via
    aliases, then the last such value (as determined by order of kwargs)
    will take precedence over other values
    """

    def wrapper(func: callable) -> callable:
        """
        Parameters
        ----------
        func : callable
            the function to wrap

        Returns
        -------
        inner : callable
            the wrapped function
        """

        def inner(*args, **kwargs):
            kwargs = {(argname if k in aliases else k): v for k, v in kwargs.items()}
            return func(*args, **kwargs)

        return inner

    return wrapper
