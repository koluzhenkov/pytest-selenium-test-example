from selenium import webdriver
from fixture.contacts import ContactsHelper
from fixture.team import TeamHelper
import allure


class Application:

    @allure.step('Running browser')
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        self.wd = webdriver.Chrome(options=chrome_options)
        self.wd.implicitly_wait(5)

        self.contacts = ContactsHelper(self)
        self.team = TeamHelper(self)
        self.home_page_url = "https://itmegastar.com/"

    def open_home_page(self):
        wd = self.wd
        wd.get(self.home_page_url)

    def find_text_on_page(self, text):
        wd = self.wd
        wd.find_element_by_xpath("//*[text()='{}']".format(text))

    @allure.step('Stopping browser')
    def destroy(self):
        self.wd.quit()
