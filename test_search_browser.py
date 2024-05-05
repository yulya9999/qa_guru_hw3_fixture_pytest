import pytest
from selene import browser, be, have


def test_search_google(browser_params):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_google_invalid_request(browser_params):
    query_string = "jtgfvcumj utgcfmjutgdcx,tgujhf xcbnm"

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(query_string).press_enter()
    browser.element('.card-section [role="heading"]').should(have.text(f'По запросу {query_string} ничего не найдено'))


def test_search_ya(browser_params):
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search-result"]').should(have.text('can be built either in a simple straightforward '
                                                             '"selenide" style or with PageObjects composed from '
                                                             'Widgets i.e. reusable element components.'))
