class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.lbl_Welcome_id = "welcome"
        self.lbl_Logout_id = "Logout"

    def clkwelcome(self):
        self.driver.find_element_by_id(self.lbl_Welcome_id).click()

    def clklogout(self):
        self.driver.find_element_by_link_text(self.lbl_Logout_id).click()

