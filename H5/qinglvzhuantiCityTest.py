#encoding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import HTMLTestRunner

class qinglvCityTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://m.kuxun.cn/"
        self.verificationErrors = [ ]
        self.accept_next_alert = True

    def test_city(self):
        driver = self.driver
        driver.get(self.base_url + "hotel-qinglvzhuanti-hangzhou.html")
        time.sleep(2)
        driver.find_element_by_link_text(u"杭州").click()
        time.sleep(4)
        driver.find_element_by_link_text(u"北京").click()

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
    testsuite.addTest(qinglvCityTest("test_city"))

    filename = '../H5Report/qinglvzhuantiCityTest.html'
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Test Result',
                description='Test Result.'
                )
    runner.run(testsuite)
