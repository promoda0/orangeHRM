import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OpenBrowser:
    def __init__(self, browser_type="chrome"):
        """
        Initialize the OpenBrowser class.
        :param browser_type: Type of browser to launch (e.g., "chrome", "firefox", "edge").
        """
        self.driver = None
        self.browser_type = browser_type.lower()

    def start_browser(self, url):
        """
        Start the browser and navigate to the specified URL.
        :param url: The URL to navigate to.
        :return: WebDriver instance.
        """
        try:
            # Initialize WebDriver based on browser type
            if self.browser_type == "chrome":
                logger.info("Launching Chrome browser...")
                self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            elif self.browser_type == "firefox":
                logger.info("Launching Firefox browser...")
                self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            elif self.browser_type == "edge":
                logger.info("Launching Edge browser...")
                self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            else:
                raise ValueError(f"Unsupported browser type: {self.browser_type}")

            # Maximize the browser window
            self.driver.maximize_window()
            logger.info("Browser window maximized.")

            # Navigate to the specified URL
            self.driver.get(url)
            logger.info(f"Navigated to URL: {url}")

            return self.driver

        except Exception as e:
            logger.error(f"Failed to start browser: {e}")
            raise

    def close_browser(self):
        """
        Close the browser.
        """
        if self.driver:
            try:
                self.driver.quit()
                logger.info("Browser closed successfully.")
            except Exception as e:
                logger.error(f"Failed to close browser: {e}")
                raise

