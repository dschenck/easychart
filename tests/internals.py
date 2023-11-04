import easychart.internals as internals


def test_flatten_singular_value():
    assert internals.flatten(1) == [1]


def test_flatten_multiple_singular_values():
    assert internals.flatten(1, 2, 3) == [1, 2, 3]


def test_flatten_multiple_depth():
    assert internals.flatten(1, [2, 3]) == [1, 2, 3]


def test_size_parsing():
    assert isinstance(internals.Size(1), internals.Size.Pixels)
    assert isinstance(internals.Size(500), internals.Size.Pixels)
    assert isinstance(internals.Size("500"), internals.Size.Pixels)
    assert isinstance(internals.Size("500px"), internals.Size.Pixels)

    assert isinstance(internals.Size(0.5), internals.Size.Percentage)
    assert isinstance(internals.Size("1%"), internals.Size.Percentage)
    assert isinstance(internals.Size("100%"), internals.Size.Percentage)


def test_size_int_values():
    assert int(internals.Size(500)) == 500
    assert int(internals.Size("500")) == 500
    assert int(internals.Size("500px")) == 500

    assert int(internals.Size("95%")) == 95


def test_size_float_values():
    assert float(internals.Size(500)) == 500
    assert float(internals.Size("500")) == 500
    assert float(internals.Size("500px")) == 500

    assert float(internals.Size(0.5)) == 0.5
    assert float(internals.Size("95%")) == 0.95
