from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# ^ potrzebujemy tego zeby miec podpowiedzi dla self.driver
#   trzeba "dziedziczyc" driver po WebDriverze though
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # <- fajnie

class EyeGamePage:

    url = "https://www.igame.com/eye-test/"

    def __init__(self, driver : WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("Iframe"))

    def click_chosen_one(self):
        #self.driver.find_element_by_css_selector('.thechosenone').click()
        self.driver.find_element(By.CSS_SELECTOR, '.thechosenone').click()

    def get_to_level(self, level):
        for i in range(level.value):
            self.click_chosen_one()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.ID, "timeleft")))

    def get_current_time(self):
        return self.driver.find_element_by_css_selector('.clock').text

    def get_reached_level(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.character-title').text

    def check_level_reached(self, level):
        assert self.driver.find_element(By.CSS_SELECTOR, '.character-title').text == level.name