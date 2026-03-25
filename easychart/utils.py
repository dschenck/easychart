from typing import Iterable, List, TypeVar, Hashable

T = TypeVar("T", bound=Hashable)


def deduplicate(lst: Iterable[T]) -> List[T]:
    """
    Return a deduplicated list of items, in the order of the
    original list

    Parameters
    ----------
    lst : iterable
        Iterable of hashable values

    Returns
    -------
    list
    """
    seen: set[T] = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
