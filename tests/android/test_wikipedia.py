import allure
from appium.webdriver.common.appiumby import AppiumBy
from allure_commons.types import Severity
from selene import have, be
from selene.support.shared import browser
from wikipedia_app.assist.selectors_xpath import settings_xpath, add_language, russian_language


@allure.tag("mobile")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Artem Mlynskij")
@allure.feature("Search")
def test_search_wikipedia():
    with allure.step('Click on "Skip"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with allure.step('type "Tesla"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'Tesla'
        )
    with allure.step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))


@allure.tag("mobile")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Artem Mlynskij")
@allure.feature("Voice Search")
def test_voice_search():
    with allure.step('Click on "Skip"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with allure.step('Click on voice search button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/voice_search_button')).click()
    with allure.step('Check for voice search launched'):
        voice_element = 'com.google.android.googlequicksearchbox:id/transcription_intent_api_main'
        browser.element((AppiumBy.ID, voice_element)).should(be.visible)


@allure.tag("mobile")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Artem Mlynskij")
@allure.feature("Empty Search")
def test_empty_search():
    with allure.step('Click on "Skip"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with allure.step('Add empty field'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            ''
        )
    with allure.step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size(0))


@allure.tag("mobile")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Artem Mlynskij")
@allure.feature("Add Wikipedia language")
def test_add_new_language():
    with allure.step('Click on "Skip"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with allure.step('Click on "More"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/nav_more_container')).click()
    with allure.step('Click on "Settings"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_drawer_settings_container')).click()
    with allure.step('Click on "Wikipedia languages"'):
        browser.element((AppiumBy.XPATH, settings_xpath)).click()
    with allure.step('Click on "Wikipedia languages"'):
        browser.element((AppiumBy.XPATH, add_language)).click()
    with allure.step('Click on "Wikipedia languages"'):
        browser.element((AppiumBy.XPATH, russian_language)).click()
    with allure.step('Click on "Wikipedia languages"'):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.texts('Wikipedia languages', 'Your languages', '1', 'EN', 'English', '2', 'RU', 'Русский', 'ADD LANGUAGE'))
