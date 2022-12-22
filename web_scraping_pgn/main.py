import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class Web_Scraping_pgn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Conf path downloads files
        options = Options()
        options.add_experimental_option("prefs", {"download.default_directory" : "/home/gnu/github/web_scraping_pgn/pgn_files"}) # Set Path

        cls.driver= webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
        driver = cls.driver
        
        cls.url = "https://www.pgnmentor.com/"
        url = cls.url
        driver.get(url)
        time.sleep(.30)


    def test_download_pgn_players_files(self):
        driver = self.driver
        
        # Navigate to pgn files page
        page_pgn_file = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/table/tbody/tr/td[3]/a').click()
        time.sleep(.30)

        # Get links pgn for download
        elemts = driver.find_elements(By.XPATH, '//table/tbody/tr/td/a[contains(@href, "players/")]')
        
        # Downloads pgn files
        for elem in elemts:
            player = elem.get_dom_attribute("href")
            url_player = self.url + player
            driver.get(url_player)
            time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'web_scraping'))