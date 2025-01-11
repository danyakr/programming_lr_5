from unittest.mock import patch
import pytest
from main import CurrencyFetcher

@pytest.fixture
def currency_fetcher():
    return CurrencyFetcher(cooldown=1)

@patch('main.CurrencyFetcher.fetch_currencies')
def test_fetch_currencies(mock_fetch, currency_fetcher, capsys):
    mock_fetch.return_value = [{'USD': ('Доллар США', ('75', '0000'))}]
    result = currency_fetcher.fetch_currencies(['R01235'])
    assert len(result) == 1
    assert result[0]['USD'] == ('Доллар США', ('75', '0000'))

@patch('main.CurrencyFetcher.fetch_currencies')
def test_visualize_currencies(mock_fetch, currency_fetcher):
    mock_fetch.return_value = [{'USD': ('Доллар США', ('75', '0000'))}]
    currency_fetcher.fetch_currencies(['R01235'])

def test_too_frequent_requests(currency_fetcher):
    currency_fetcher.fetch_currencies(['R01235'])
    with pytest.raises(Exception, match="Запросы можно делать не чаще, чем раз в 1 секунд"):
        currency_fetcher.fetch_currencies(['R01235'])
