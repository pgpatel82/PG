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
        self.assertIn("Auto Auction - Copart USA - Salvage Cars for Sale in Online Car Auctions", self.driver.title)
        #elements = self.driver.find_element(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        elements = self.driver.find_element(By.XPATH, "//*[@id=\"tabTrending\"]//ul")
        items = elements.find_elements_by_tag_name("li")
        print(items)
        for item in items:
            print(item.text + "-->" item.href)
            #print(item.getattribute("href")


if __name__ == '__main__':
    unittest.main()
