# tests/test_data_loading.py
import pytest
import pandas as pd
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(PROJECT_ROOT, 'data', 'raw')
PROCESSED_DIR = os.path.join(PROJECT_ROOT, 'data', 'processed')

UNIFIED_CSV = os.path.join(RAW_DIR, 'ethiopia_fi_unified_data.csv')
ENRICHED_CSV = os.path.join(PROCESSED_DIR, 'enriched_fi_unified_data.csv')


@pytest.fixture
def load_unified_data():
    """Fixture to load raw unified data or raise meaningful error"""
    if not os.path.exists(UNIFIED_CSV):
        pytest.skip("Raw unified CSV not found - run conversion step first")
    return pd.read_csv(UNIFIED_CSV, low_memory=False)


@pytest.fixture
def load_enriched_data():
    """Fixture to load enriched data from Task 1"""
    if not os.path.exists(ENRICHED_CSV):
        pytest.skip("Enriched CSV not found - run Task 1 notebook first")
    return pd.read_csv(ENRICHED_CSV, low_memory=False)


def test_raw_data_exists_and_has_expected_columns(load_unified_data):
    df = load_unified_data
    assert not df.empty, "Raw data should not be empty"
    expected_cols = ['record_id', 'record_type', 'category', 'pillar', 'indicator', 'indicator_code']
    missing = [col for col in expected_cols if col not in df.columns]
    assert not missing, f"Missing required columns: {missing}"


def test_record_types_are_valid(load_unified_data):
    df = load_unified_data
    valid_types = {'observation', 'event', 'impact_link', 'target'}
    invalid = df[~df['record_type'].isin(valid_types)]['record_type'].unique()
    assert len(invalid) == 0, f"Invalid record_types found: {invalid}"


def test_enriched_data_has_more_rows_than_raw(load_enriched_data, load_unified_data):
    raw_rows = load_unified_data.shape[0]
    enriched_rows = load_enriched_data.shape[0]
    assert enriched_rows > raw_rows, \
        f"Enriched data ({enriched_rows} rows) should have more rows than raw ({raw_rows})"


def test_enriched_data_has_new_observations_from_2025(load_enriched_data):
    df = load_enriched_data
    recent = df[df['observation_date'].str.contains('2025', na=False, regex=False)]
    assert len(recent) >= 5, "Expected at least 5 new 2025 observations (Findex, penetration, etc.)"
    assert 'Global Findex 2025' in df['source_name'].values, "Findex 2025 should be present"


def test_enriched_data_has_NDPS_event(load_enriched_data):
    df = load_enriched_data
    ndps_events = df[(df['record_type'] == 'event') & (df['indicator'].str.contains('NDPS', na=False))]
    assert len(ndps_events) >= 1, "NDPS 2026-2030 launch event should be in enriched data"


def test_confidence_values_are_valid(load_enriched_data):
    df = load_enriched_data
    
    # Only check rows where confidence is filled (events often don't have it)
    filled_conf = df[df['confidence'].notna()]
    
    valid_conf = {'high', 'medium', 'low', 'estimated'}
    invalid = filled_conf[~filled_conf['confidence'].isin(valid_conf)]['confidence'].unique()
    
    assert len(invalid) == 0, f"Invalid confidence values found in filled rows: {invalid}"