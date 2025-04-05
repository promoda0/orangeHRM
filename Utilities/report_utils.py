import os
from datetime import datetime

def capture_screenshot(driver, nodeid):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = nodeid.split("::")[-1].replace("[", "_").replace("]", "")
    screenshot_dir = os.path.join(os.getcwd(), "Reports", "Screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshot_dir, filename)
    driver.save_screenshot(filepath)
    return os.path.relpath(filepath, os.getcwd())