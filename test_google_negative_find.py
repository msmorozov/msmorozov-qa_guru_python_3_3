import pytest
from selene.support.shared import browser


def test_negative_case(open_browser):
    negative_search = 'uefpiqwf w1efpqwgefqbve'
    negative_search_result = 'About 0 results'

    browser.element('[name="q"]').should(be.blank).type(negative_search).press_enter()
    browser.element('[id="result-stats"]').should(have.text(negative_search_result))