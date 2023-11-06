import pytest
import pathlib
import os
import json
import textwrap


@pytest.fixture
def datadir() -> pathlib.Path:
    """
    Returns the directory where regression tests are stored
    """
    return pathlib.Path(os.path.join(os.path.dirname(__file__), "data"))


@pytest.fixture
def regression(
    datadir: pathlib.Path,
    request: pytest.FixtureRequest,
):
    """
    Fixture designed to provide a regression test for the given
    test
    """

    class RegressionTest:
        """
        Regression test
        """

        def __init__(self, datadir: pathlib.Path, request: pytest.FixtureRequest):
            self.datadir = datadir
            self.request = request

        @property
        def name(self) -> str:
            """
            Returns test name
            """
            return self.request.module.__name__

        @property
        def filename(self) -> pathlib.Path:
            """
            Returns filename of the regression output

            Returns
            -------
            pathlib.Path
            """
            return os.path.join(self.datadir, f"{self.name}.regtest.json")

        def exists(self) -> bool:
            """
            Returns True if the regression output already exits

            Returns
            -------
            bool
            """
            return os.path.exists(self.filename)

        def load(self) -> dict:
            """
            Read the existing regression output

            Returns
            -------
            dict
            """
            with open(self.filename, "r") as file:
                return json.load(file)

        def write(self, data, **kwargs):
            """
            Write a new regression test output

            Returns
            -------
            None
            """
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4, **kwargs)
            return True

        def check(self, data: dict, **kwargs):
            """
            Checks for differences between the passed data, and any previously-computed
            data.
            """
            if self.request.config.getoption("--regenerate-all"):
                return self.write(data, **kwargs)

            if not self.exists():
                if self.request.config.getoption("--regenerate-missing"):
                    return self.write(data, **kwargs)

                return pytest.fail(
                    textwrap.dedent(
                        f"""
                        regression test for '{self.name}' failed because previously computed data does not exist; run 'pytest --regenerate-missing' to generate the missing data
                        """
                    )
                )

            if self.load() != data:
                if self.request.config.getoption("--regenerate-failing"):
                    return self.write(data, **kwargs)

                return pytest.fail(
                    textwrap.dedent(
                        f"""
                        regression test for '{self.name}' failed because recomputed data differs from previously computed data; 
                        """
                    )
                )

            return True

    return RegressionTest(datadir, request=request)
