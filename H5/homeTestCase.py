#encoding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import HTMLTestRunner


class homeTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://m.kuxun.cn/"
        self.verificationErrors = [ ]
        self.accept_next_alert = True

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    testsuite.addTest(homeTestCase("test_city"))

    testResultHtml = '../H5Report/homeTestCase.html'
    fp = file(testResultHtml, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Test Result',
                description='Test Result.'
                )
    runner.run(testsuite)

