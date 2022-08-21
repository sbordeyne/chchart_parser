from pathlib import Path

import pytest

from chchart_parser.chart import Chart


@pytest.fixture
def test_data_path() -> Path:
    return Path(__file__).parent / 'data'


@pytest.fixture
def chart(test_data_path: Path) -> str:
    return Chart((test_data_path / 'notes.chart'))
