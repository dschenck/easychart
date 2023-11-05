# Regression testing

> Regression testing is designed to ensure that previously developed and tested software still performs as expected after a change.

## Regression tests

Each `.py` file under the `regression-tests/tests` folder should contain a single `regress` test case which generates an `easychart.Chart` instance and passes it to a `RegressionTest.check` fixture.

Possible outcomes:

1. The regression test was previously generated, and the outputof the re-run matches existing output. The regression test succeeds.

2. The regression test was previously generated but a re-run does not match the existing output. This means that either:

   - a new regression was introduced by faulty code change: the regression test failed
   - the previous regression test generated faulty output: the regression test should be regenerated

3. The regression test was never run and no previous output exists to compare to: output of the regression test should be regenerated

## Possible flags

Depending on the above scenario, you can run the tests with the below flags.

| Flag                   | Description                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- |
| `--regenerate-missing` | Regenerate regression test output data for cases where such data does not exist |
| `--regenerate-failing` | Regenerate regression test output data for failing cases                        |
| `--regenerate-all`     | Regenerate regression test output data for all cases                            |
