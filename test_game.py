from selenium.webdriver import Firefox
from eye_game import EyeGamePage
from browser import get_driver

def test_kret_level():
    driver = get_driver()
    eye_game = EyeGamePage(driver)
    eye_game.load()
    #eye_game.click_chosen_one()
    eye_game.get_to_level(30)
    eye_game.check_level_reached()
    #assert eye_game.get_reached_level() == "ROBOT"
    driver.close()
