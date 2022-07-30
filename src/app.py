from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Navigation options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# URL to scrape.
SCRAPE_URL = 'https://google.com'


def init_driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=options)
    driver.get(SCRAPE_URL)
    return driver


def main():
    driver = init_driver()
    driver.quit()


if __name__ == '__main__':
    main()
