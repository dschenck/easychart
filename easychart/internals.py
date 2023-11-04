import collections
import numbers


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


class Size:
    """
    Utility class designed to represent sizes (pixels and percentages)
    """

    class Pixels(str):
        """
        Absolute size (in pixels)
        """

        def __new__(cls, value):
            if isinstance(value, numbers.Number):
                value = f"{value:.0f}px"
            if not value.endswith("px"):
                value = f"{value}px"
            return super().__new__(cls, value)

        def __int__(self):
            return int(self[:-2])

        def __float__(self):
            return float(self[:-2])

        def resolve(self, parent):
            return self

    class Percentage(str):
        """
        Relative size (in percentage of parent)
        """

        def __new__(cls, value):
            if isinstance(value, numbers.Number):
                value = f"{value}%"
            if not value.endswith("%"):
                value = f"{value}%"
            return super().__new__(cls, value)

        def __int__(self):
            return int(self[:-1])

        def __float__(self):
            return float(self[:-1]) / 100

        def resolve(self, parent):
            return Size(float(self) * float(Size(parent)))

    def __new__(cls, value):
        if isinstance(value, (Size.Percentage, Size.Pixels)):
            return value
        if isinstance(value, str):
            if value.endswith("%"):
                return Size.Percentage(value)
            elif value.endswith("px"):
                return Size.Pixels(value)
            elif value.isnumeric():
                return Size.Pixels(value)
        if isinstance(value, (float, int)):
            if value < 1:
                return Size.Percentage(100 * value)
            else:
                return Size.Pixels(value)
        raise ValueError(f"Unrecognized size '{value}'")
