import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class bonuschallange1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_rokusearch(self):
        self.driver.get("https://help.sling.com/")
        self.assertIn("Help Center", self.driver.title)
        self.driver.find_element(By.ID, "support-search-input").click()
        self.driver.find_element(By.ID, "support-search-input").send_keys("Roku")
        self.driver.find_element_by_xpath("//*[@id=\"hc-search-form\"]//button").click()
        self.driver.implicitly_wait(15)
        assert "No results found." not in self.driver.page_source
        result = self.driver.find_element_by_xpath("/html/body/div[3]/div//h4[3]").text
        assert (result == 'You searched for: Roku'), "Roku search result not found."
        print("Roku Search Result Found.")
        elements=self.driver.find_elements_by_xpath("/html/body//div[2]/ul/section")
        #print(elements)
        for item in elements:
            #print(item)
            print(item.text)

if __name__ == '__main__':
    unittest.main()