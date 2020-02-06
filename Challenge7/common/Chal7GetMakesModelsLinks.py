from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from array import *

class Chal7GetMakesModelsLinks:
    def __init__ (self, driver):
        self.driver = driver

    def getlinks(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        n = len(elements)
        m = 2
        arr = [[0 for x in range(m)] for y in range(n)]
        i = 0
        for item in elements:
            j = 0
            arr[i][j] = item.text
            #print(arr[i][j])
            j = j+1
            arr[i][j] = item.get_attribute("href")
            #print(arr[i][j])
            i = i + 1
        #print(len(arr))
        return arr

    #def checklinks(self, ListLinkarray):

