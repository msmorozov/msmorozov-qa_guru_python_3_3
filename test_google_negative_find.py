import pytest
from selene.support.shared import browser
from selene import have, be


def test_negative_case(open_browser):
    negative_search = 'uefpiqwf w1efpqwgefqbve'
    negative_search_result = 'About 0 results'

    browser_point_serch = '[name="q"]'
    browser_point_result = '[id="result-stats"]'

    browser.element(browser_point_serch).should(be.blank).type(negative_search).press_enter()
    browser.element(browser_point_result).should(have.text(negative_search_result))