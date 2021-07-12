import time
import unittest
import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from utilities.util import Util
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/home/bado/BitbyBit/Selenium/automation_testing/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVC):
        self.courses.enterCourseName(courseName)
        self.courses.selectCoursetoEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvc=ccCVC)
        time.sleep(3)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrolment", result,
                          "Enrollment Failed Verification")
        self.driver.find_element_by_link_text("ALL COURSES").click()


