class HOME:
    home_link='//*[@id="menu-item-43"]/a'
    practice_link='//*[@id="menu-item-20"]/a'
    logout_button='//*[@id="loop-container"]/div/article/div[2]/div/div/div/a'

    def __init__(self,drivers):
        self.drivers=drivers

    def click_home_link(self):
        self.drivers.find_element('xpath',self.home_link).click()
    def click_practice_link(self):
        self.drivers.find_element('xpath',self.practice_link).click()
    def click_logout_button(self):
        self.drivers.find_element('xpath',self.logout_button).click()