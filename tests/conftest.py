import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--regenerate-missing",
        action="store_true",
        default=False,
        help="Regenerate regression test output data for cases where such data does not exist",
    )

    parser.addoption(
        "--regenerate-failing",
        action="store_true",
        default=False,
        help="Regenerate regression test output data for failing cases",
    )

    parser.addoption(
        "--regenerate-all",
        action="store_true",
        default=False,
        help="Regenerate regression test output data for all cases",
    )
