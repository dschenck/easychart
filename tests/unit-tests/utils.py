import pytest

from easychart.utils import deduplicate


def test_deduplicate_ints():
    data = [1, 2, 2, 3, 1]
    assert deduplicate(data) == [1, 2, 3]


def test_deduplicate_tuples_and_order():
    data = [(1, 2), (1, 2), (2,)]
    assert deduplicate(data) == [(1, 2), (2,)]


def test_deduplicate_generator_preserves_order():
    gen = (x for x in [3, 1, 3, 2])
    assert deduplicate(gen) == [3, 1, 2]


def test_deduplicate_empty():
    assert deduplicate([]) == []


def test_deduplicate_unhashable_raises_typeerror():
    # Passing unhashable elements (lists) should raise at runtime
    with pytest.raises(TypeError):
        deduplicate([[1], [1]])
