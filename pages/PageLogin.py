
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.txt_UserName_id = "txtUsername"
        self.txt_Password_id = "txtPassword"
        self.btn_Login_id = "btnLogin"

    def set_username(self, username):
        self.driver.find_element_by_id(self.txt_UserName_id).clear()
        self.driver.find_element_by_id(self.txt_UserName_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.txt_Password_id).clear()
        self.driver.find_element_by_id(self.txt_Password_id).send_keys(password)

    def clk_login(self):
        self.driver.find_element_by_id(self.btn_Login_id).click()

    def assererrorMessage(self):
        self.assertEqual("Employee is terminated", self.driver.find_element_by_id("spanMessage").text)
