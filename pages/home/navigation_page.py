import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from  base.basepage import  BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _all_courses= "ALL COURSES"
    _my_courses = "MY COURSES"
    _practice = "PRACTICE"
    _user_icon = "dropdownMenu1"


    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")
    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")
    def navigateToAllPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")
    def navigateToUserSettings(self):
        self.elementClick(locator=self._user_icon)

