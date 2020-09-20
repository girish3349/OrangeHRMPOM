import time
from pages.PageLogin import LoginPage


class commonMethods:
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

        self.menu_PIM_id = "menu_pim_viewPimModule"
        self.menu_AddEmployee_id = "menu_pim_addEmployee"
        self.menu_EmployeeList_id = "menu_pim_viewEmployeeList"

        self.menu_Admin_id = "menu_admin_viewAdminModule"
        self.menu_Job_Id = "menu_admin_Job"
        self.menu_JobTitle_Id = "menu_admin_viewJobTitleList"

    def login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        loginpage = LoginPage(driver)
        loginpage.set_username("Admin")
        loginpage.set_password("admin123")
        loginpage.clk_login()
        #loginpage.assererrorMessage()


    # Navigation for two level menu
    def naviageToMenu(self, mainMenu, subMenu1, subMenu2 = None):
        self.driver.find_element_by_id(mainMenu).click()
        self.driver.find_element_by_id(subMenu1).click()
        if subMenu2: # 
            menu = self.driver.find_element_by_id(subMenu2)
            self.actions.move_to_element(menu).perform()
            time.sleep(1)
            self.actions.click(menu).perform()

    def navigatetoAddEmployee(self):
        self.naviageToMenu(self.menu_PIM_id, self.menu_AddEmployee_id)

    def navigatetoJobtitle(self):
        self.naviageToMenu(self.menu_Admin_id, self.menu_Job_Id, self.menu_JobTitle_Id)

    def navigatetoEmployeeList(self):
        self.driver.find_element_by_id(self.menu_PIM_id).click()
        self.driver.find_element_by_id(self.menu_EmployeeList_id).click()
