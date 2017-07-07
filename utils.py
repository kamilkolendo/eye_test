import time

def wait_until(condition, timeout=10, raise_exception=True, msg=""):

    t = time.time()
    while time.time() - t < timeout:
        if condition():
            return True
