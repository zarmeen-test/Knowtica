class LOGIN:
    username='//*[@id="username"]'
    password='//*[@id="password"]'
    submit='//*[@id="submit"]'

    def __init__(self,drivers):
        self.drivers=drivers

    def enter_username(self,input):
        self.drivers.find_element('xpath',self.username).send_keys(input)
    def enter_password(self,input):
        self.drivers.find_element('xpath',self.password).send_keys(input)
    def click_submit(self):
        self.drivers.find_element('xpath',self.submit).click()
