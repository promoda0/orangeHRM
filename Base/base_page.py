from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException
import logging
from Utilities.test_data_reader import TestDataReader
from selenium.webdriver.common.keys import Keys



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.default_timeout = 10  # Centralized timeout setting
        self.data_reader = TestDataReader()

    def _find_element(self, locator):
        """Internal method to find a single element with explicit wait."""
        try:
            return WebDriverWait(self.driver, self.default_timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element not visible after {self.default_timeout}s: {locator}")
            raise
        except NoSuchElementException:
            logger.error(f"Element not found in DOM: {locator}")
            raise

    def click(self, locator):
        """Click on an element with visibility check."""
        try:
            element = self._find_element(locator)
            logger.info(f"Clicking on element: {locator}")
            element.click()
        except Exception as e:
            logger.error(f"Failed to click on element: {locator}")
            raise e

    def send_keys(self, locator, text):
        """Enter text into an input field."""
        try:
            element = self._find_element(locator)
            logger.info(f"Entering text '{text}' into {locator}")
            element.clear()
            element.send_keys(text)
        except Exception as e:
            logger.error(f"Failed to enter text into element: {locator}")
            raise e

    def get_text(self, locator):
        """Get text from a visible element."""
        try:
            element = self._find_element(locator)
            text = element.text
            logger.info(f"Retrieved text: '{text}' from {locator}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text from element: {locator}")
            raise e

    def is_element_visible(self, locator):
        """Check if element is visible without throwing exceptions."""
        try:
            return self._find_element(locator).is_displayed()
        except:
            return False
    # Example usage in page objects
    def load_test_data(self,file_path):
        return self.data_reader.read_json(file_path)

    def clear_field(self, locator, timeout=None, verify_cleared=True):
        """
        Robust field clearing with verification
        :param locator: Tuple (By strategy, locator)
        :param timeout: Maximum wait time in seconds
        :param verify_cleared: Verify field was actually cleared
        """
        timeout = timeout or self.default_timeout
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            try:
                self.logger.info(f"Clear attempt {attempts + 1} for {locator}")

                # Wait for element to be interactable
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )

                # Strategy 1: Standard clear
                element.clear()
                self.logger.debug("Used standard clear() method")

                # Strategy 2: Keyboard fallback
                if element.get_attribute('value') or element.text:
                    self.logger.debug("Trying keyboard clear")
                    element.send_keys(Keys.CONTROL + 'a')
                    element.send_keys(Keys.DELETE)

                # Strategy 3: JavaScript nuclear option
                if verify_cleared and (element.get_attribute('value') or element.text):
                    self.logger.debug("Trying JavaScript clear")
                    self.driver.execute_script("arguments[0].value = '';", element)

                # Final verification
                if verify_cleared:
                    current_value = element.get_attribute('value') or element.text
                    if current_value:
                        raise ValueError(f"Field not cleared! Current value: '{current_value}'")

                self.logger.info(f"Successfully cleared {locator}")
                return

            except StaleElementReferenceException:
                self.logger.warning("Element went stale, retrying...")
                attempts += 1

            except ElementNotInteractableException:
                self.logger.error(f"Element not interactable: {locator}")
                raise

            except Exception as e:
                self.logger.error(f"Clear failed: {str(e)}")
                raise

        raise RuntimeError(f"Failed to clear {locator} after {max_attempts} attempts")