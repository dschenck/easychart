import pytest
import polars as pl
import pandas as pd

import easychart
from easychart.encoders import default


class TestPolarsSupport:
    """Tests for Polars DataFrame/Series support via narwhals"""

    def test_polars_series(self):
        ps = pl.Series("test_series", [1, 2, 3])
        chart = easychart.new()
        chart.plot(ps)
        assert chart.series[0]["data"] == [1, 2, 3]
        assert chart.series[0]["name"] == "test_series"

    def test_polars_series_unnamed(self):
        ps = pl.Series([1, 2, 3])
        chart = easychart.new()
        chart.plot(ps)
        assert chart.series[0]["data"] == [1, 2, 3]

    def test_polars_dataframe(self):
        df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
        chart = easychart.new()
        chart.plot(df)
        assert chart.series[0]["data"] == [(1, 3), (2, 4)]

    def test_polars_heatmap(self):
        df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
        chart = easychart.heatmap(df)
        assert chart.chart.type == "heatmap"
        # Verify data was converted and plotted
        assert len(chart.series[0]["data"]) == 9  # 3x3 grid


class TestPandasRegression:
    """Ensure pandas behavior is unchanged"""

    def test_pandas_series_with_index(self):
        ps = pd.Series([10, 20, 30], index=[0, 1, 2], name="pandas_test")
        chart = easychart.new()
        chart.plot(ps)
        # Pandas includes index by default
        assert chart.series[0]["data"] == [[0, 10], [1, 20], [2, 30]]
        assert chart.series[0]["name"] == "pandas_test"

    def test_pandas_series_without_index(self):
        ps = pd.Series([10, 20, 30], name="pandas_test")
        chart = easychart.new()
        chart.plot(ps, index=False)
        assert chart.series[0]["data"] == [10, 20, 30]

    def test_pandas_dataframe(self):
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        chart = easychart.new()
        chart.plot(df)
        # Pandas includes index
        assert chart.series[0]["data"] == [[0, 1, 3], [1, 2, 4]]


class TestEncoderSupport:
    """Test JSON encoder handles Polars types"""

    def test_encoder_polars_series(self):
        ps = pl.Series("test", [1, 2, 3])
        result = default(ps)
        assert result == [1, 2, 3]

    def test_encoder_polars_dataframe(self):
        df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
        result = default(df)
        assert result == [(1, 3), (2, 4)]

    def test_encoder_pandas_still_works(self):
        ps = pd.Series([1, 2, 3])
        result = default(ps)
        assert result == [1, 2, 3]
