import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from common.TopNavSearch import TopNavSearch


class challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_checkforSkyLine(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        self.driver.implicitly_wait(10)

        query = "Nissan"
        input_model = "SKYLINE"
        TopNavSearch(self.driver).runSearch(query)

        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, "//table[@id='serverSideDataTable']//a[@data-uname='lotsearchLotnumber']")))

        models = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotmodel']")
        lot_numbers = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//a[@data-uname='lotsearchLotnumber']")

        model_list = []

        for model in models:
            model_list.append(model.text)

        try:
            position = model_list.index(input_model)
           # position = model_list.index("ARMADA")
            skyline_lot = lot_numbers[position]
            skyline_lot.click()
            WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[@data-uname="lotdetailTitledescription"]')))
            #self.driver.save_screenshot("challenge_6_screenshot1.png")
        except ValueError:
            print("Model SKYLINE not found -- See the Captured Screenshot")
            self.driver.save_screenshot("challenge_6_screenshot.png")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()