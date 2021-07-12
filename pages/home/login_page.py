import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from  base.basepage import  BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()
        time.sleep(2)

    def verifyLoginSuccussful(self):
        result = self.isElementPresent("dropdownMenu1", "id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(), 'invalid')]",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.nav.navigateToUserSettings()
        self.elementClick(locator="Logout",locatorType="link")