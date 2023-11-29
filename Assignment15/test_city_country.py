from city_functions import CityCountry
import pytest

def test_city_country():
    assert CityCountry('Philadelphia', 'United States') == 'Philadelphia, United States, 0'

def test_population():
    assert CityCountry('Philadelphia', 'United States', '1000000') == 'Philadelphia, United States, 1000000'
