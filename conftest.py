import pytest
from browser import get_driver

def pytest_exception_interact(node, call, report):
    get_driver().save_screenshot(f"{node.name}_error.png") # <-sprytnie, zrobilismy breakpoint i grzebalismy w zmiennych zeby odkryc ze w nodzie jest "name"

@pytest.fixture(scope="module")
def driver():
    return get_driver()
# ^kazdy test ktory bedzie potrzebowal drivera ma otrzymac ten driver