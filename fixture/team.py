class TeamHelper:

    def __init__(self, app):
        self.app = app

    def open_team_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.header__menu a[href="/team"]').click()


