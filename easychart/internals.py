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


class Percentage:
    def __init__(self, value):
        if isinstance(value, str) and value.endswith("%"):
            self.value = float(value[:-1])
        else:
            self.value = float(value)

    def __str__(self):
        return f"{self.value}%"

    def resolve(self, parent):
        """
        Convert to pixels
        """
        return parent * self.value / 100


class Pixels:
    def __init__(self, value):
        if isinstance(value, str) and value.endswith("px"):
            self.value = float(value[:-2])
        else:
            self.value = float(value)

    def __str__(self):
        return f"{self.value}px"

    def resolve(self, parent):
        return self.value


class Size:
    def __new__(cls, value):
        if isinstance(value, (Percentage, Pixels)):
            return value
        if isinstance(value, str):
            if value.endswith("%"):
                return Percentage(value)
            elif value.endswith("px"):
                return Pixels(value)
            elif value.isnumeric():
                return Pixels(value)
        if isinstance(value, (float, int)):
            if value < 1:
                return Percentage(100 * value)
            else:
                return Pixels(value)
        raise ValueError(f"Unrecognized size '{value}'")

