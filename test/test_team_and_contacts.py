import pytest
import allure


@pytest.mark.parametrize('text', ['Семён Якушев'])
def test_find_text_on_team_page(app, text):
    with allure.step('Open ' + app.home_page_url):
        app.open_home_page()
    with allure.step('Click "Команда"'):
        app.team.open_team_page()
    with allure.step('Find text: ' + text):
        app.find_text_on_page(text)


@pytest.mark.parametrize('name', ['Захар'])
def test_fill_name(app, name):
    with allure.step('Open ' + app.home_page_url):
        app.open_home_page()
    with allure.step('Click "Контакты"'):
        app.contacts.open_contacts_page()
    with allure.step('Fill field "Имя, name: ' + name):
        app.contacts.fill_name(name)
