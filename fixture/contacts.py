class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.header__menu a[href="/contacts"]').click()

    def fill_name(self, name):
        wd = self.app.wd
        wd.find_element_by_name('name').send_keys(name)
