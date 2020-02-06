import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.TopNavSearch import TopNavSearch
import time

class challenge5 (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_checkForModel(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        self.driver.implicitly_wait(10)

        query = "Porsche"
        TopNavSearch(self.driver).runSearch(query)

        self.driver.find_element(By.XPATH, "//select[@name='serverSideDataTable_length']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//option[@value='100']").click()
        self.driver.implicitly_wait(10)
        time.sleep(30)

        all_models = self.driver.find_elements(By.XPATH,"//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotmodel']")
        #print(all_models)
        models = []
        for model in all_models:
            #print(model.text)
            models.append(model.text)

        uniquemodelset = set(models)
        uniquemodeldict = {str(list(uniquemodelset)[0]): 0}

        for unique_model in uniquemodelset:
            uniquemodeldict.update({unique_model: 0})

        for unique_model in uniquemodelset:
            for model in models:
                if model == unique_model:
                    uniquemodeldict[unique_model] += 1
            print(unique_model + ": " + str(uniquemodeldict[unique_model]))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
