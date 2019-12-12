import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3forloop(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        self.driver.implicitly_wait(10)
        #elements = self.driver.find_element(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        for item in elements:
            print(item.text + "-->" + item.get_attribute("href"))

    def test_challenge3whileloop(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        self.driver.implicitly_wait(10)
        #elements = self.driver.find_element(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[3]//a")
        i = 0
        while i < len(elements):
            print(elements[i].text + "-->" + elements[i].get_attribute("href"))
            i = i+1

if __name__ == '__main__':
    unittest.main()
