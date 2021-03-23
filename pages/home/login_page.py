from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    _sel_link_login = "//div[contains(text(),'Sign Up or Log In')]"
    _sel_field_email = "email"
    _sel_field_password = "password"
    _sel_button_login = "//input[@value='Login']"

    def navigateToLogin(self):
        self.elementClick(self._sel_link_login, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email,self._sel_field_email)

    def enterPassword(self, password):
        self.sendKeys(password,self._sel_field_password)

    def submitLogin(self):
        self.elementClick(self._sel_button_login, locatorType="xpath")

    def login(self, email="", password=""):
        self.navigateToLogin()
        self.enterEmail(email)
        self.enterPassword(password)
        self.submitLogin()

    def verifyLoginSuccessful(self):
        return self.isElementPresent("MY COURSES", locatorType="linktext")

    def verifyLoginFailed(self):
        return self.isElementPresent("//span[contains(text(),'username or password is invalid')]", locatorType="xpath")
