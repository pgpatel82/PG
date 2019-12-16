import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class bonuschallange2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_channellistorange(self):
        self.driver.get("https://sling.com/")
        self.assertIn("Live TV Streaming | Sling TV", self.driver.title)
        self.driver.find_element_by_xpath("//*[@id=\"planOne\"]").click()
        self.driver.implicitly_wait(5)
        elements = self.driver.find_elements_by_xpath("//*[@id=\"channelList\"]/li/img")
        num = len(elements)
        print("Total Number of Channels in Orange packs: ", num)
        for item in elements:
            #print(item)
            print(item.get_attribute("title"))


if __name__ == '__main__':
    unittest.main()
