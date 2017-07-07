from eye_game import EyeGamePage
import pytest

from collections import namedtuple
level = namedtuple("level", ['name', 'value']) # <-niezmienialne odpowiedniki list
# ^ to to samo co zalozenie klasy z polami name i value, ale jest krotsze i mozna po tym iterowac

ROBOT = level(name='ROBOT', value=30)
JASTRZAB = level(name='JASTRZYB', value=25)

@pytest.mark.parametrize("level",[JASTRZAB, ROBOT])
def test_level(driver, level):
    eye_game = EyeGamePage(driver)
    eye_game.load()
    eye_game.get_to_level(level=level)
    eye_game.check_level_reached(level=level)
    # driver.close()

# @pytest.mark.smoke_test # <- etykieta, mozemy opisac grupe testow zeby np najpierw wywolac najbardziej krytyczne
