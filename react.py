from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def scrape(url, xpath, scope):
    chrome_options = Options()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    wait = WebDriverWait(driver, 4)

    if scope.lower() == 'all':
        print('entire')
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        text_content = driver.find_element(By.TAG_NAME, 'body').text
    elif scope.lower() == 'selective':
        print('selective')
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = driver.find_element(By.XPATH, xpath)
        text_content = element.text

    driver.quit()
    return text_content


if __name__ == "__main__":
    text = scrape('https://www.bankbazaar.com/credit-card/federal-bankbazaar-credit-card.html',
                  '/html/body/div[3]/div/div[7]/div/div')
    print(text)
