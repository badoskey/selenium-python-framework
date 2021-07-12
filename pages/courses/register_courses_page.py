import time
import utilities.custom_logger as cl
import logging
from  base.basepage import  BasePage


class RegisterCoursesPage(BasePage):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _search_box = "//input[@id='search']"
    _search_button = "//button[@type='submit']"
    _course = "//h4[contains(text(),'{0}')]"
    _all_courses = ""
    _enroll_button = "//button[text()='Enroll in Course']"
    _cc_num = "//*[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"    #name
    _cc_cvc = "cvc"         #name
    _submit_enroll = "//*[@id='checkout-form']/div[2]/div[3]/div/div[1]/div[2]/div/button[1]"
    _enroll_error_message = "//span[text()='Your card number is incomplete.']"

    #Element Interaction

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType="xpath")
        self.elementClick(self._search_button, locatorType="xpath")

    def selectCoursetoEnroll(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName),locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def enterCardNum(self,num):
        time.sleep(2)
        self.SwitchFrameByIndex(self._cc_num,  locatorType="xpath")
        self.sendKeysWhenReady(num, self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        time.sleep(2)
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVC(self, cvc):
        time.sleep(2)
        self.SwitchFrameByIndex(self._cc_cvc, locatorType="name")
        self.sendKeys(cvc, self._cc_cvc, locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvc):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVC(cvc)

    def enrollCourse(self,num="" ,exp="" ,cvc=""):
        self.clickOnEnrollButton()
        self.webScroll("down")
        self.enterCreditCardInformation(num,exp,cvc)


    def verifyEnrollFailed(self):
        result = self.isEnabled(self._submit_enroll, "xpath", info="Enroll Button")
        return not result