# tests/test_forecasting.py
import pytest
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Mock historical ownership data from challenge (2011-2024)
@pytest.fixture
def mock_ownership_series():
    years = [2011, 2014, 2017, 2021, 2024]
    values = [14, 22, 35, 46, 49]
    df = pd.DataFrame({'year': years, 'ownership': values})
    return df


def test_linear_trend_model_fits(mock_ownership_series):
    X = sm.add_constant(mock_ownership_series['year'])
    y = mock_ownership_series['ownership']
    model = sm.OLS(y, X).fit()

    assert model.rsquared > 0.90, "Linear trend should explain >90% variance in Findex data"
    assert model.params.iloc[1] > 0, ...
    assert model.pvalues.iloc[1] < 0.05, ...

def test_forecast_2025_2027_gives_reasonable_values(mock_ownership_series):
    X = sm.add_constant(mock_ownership_series['year'])
    y = mock_ownership_series['ownership']
    model = sm.OLS(y, X).fit()

    future_years = np.array([2025, 2026, 2027])
    X_future = sm.add_constant(future_years)
    preds = model.predict(X_future)

    assert len(preds) == 3, "Should produce exactly 3 predictions"
    assert all(pred > 49 for pred in preds), "Forecasts should be above current 49%"
    assert preds[2] < 70, "2027 forecast should be realistic (below NFIS-II target 70%)"


@pytest.mark.parametrize("aggfunc", ['last', 'mean', 'first'])
def test_pivot_table_handles_duplicates(aggfunc):
    # Mock data with duplicates (like your enablers issue)
    mock_df = pd.DataFrame({
        'date': ['2021-12-31', '2021-12-31', '2025-12-31', '2025-12-31'],
        'indicator': ['ACC_OWNERSHIP', 'ACC_OWNERSHIP', 'ACC_MOBILE_PEN', 'ACC_MOBILE_PEN'],
        'value': [46.0, 49.0, 61.4, 68.4]
    })

    pivot = mock_df.pivot_table(
        index='date',
        columns='indicator',
        values='value',
        aggfunc=aggfunc
    )

    assert pivot.shape[0] == 2, "Should collapse to 2 unique dates"
    assert not pivot.isna().all().all(), "Pivoted table should have some values"