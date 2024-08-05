from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 21
PROMISED_UP = 30
CHROME_DRIVER_PATH = "/Users/user/.cache/selenium/chromedriver/mac-arm64/127.0.6533.88/chromedriver"
X_USERNAME = "@itsfornothing12"
X_EMAIL = "kalidmohamed566@gmail.com"
X_PASSWORD = "Haha123@&$"

# Keep Chrome browser open after program finishes
CHROME_OPTION = webdriver.ChromeOptions()
CHROME_OPTION.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self, chrome_options):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[1]/a')
        start_button.click()
        sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                       '2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        sleep(10)
        user_input = self.driver.find_element(By.NAME, 'text')
        user_input.send_keys(X_USERNAME)
        sleep(1)
        user_input.send_keys(Keys.ENTER)

        # sleep(2)
        # email_input = self.driver.find_element(By.NAME, 'text')
        # email_input.send_keys(X_EMAIL)
        # sleep(1)
        # email_input.send_keys(Keys.ENTER)

        sleep(2)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(X_PASSWORD)
        sleep(1)
        password_input.send_keys(Keys.ENTER)

        sleep(10)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                   '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                   '1]/div/div/div/div[2]/div['
                                                   '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                                   '1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet providers in Ethiopia, Why is my internet speed {self.down}down/"
                        f"{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        sleep(2)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                         '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                         '2]/div[2]/div/div/div/button')
        post_button.click()


starter = InternetSpeedTwitterBot(CHROME_OPTION)
starter.get_internet_speed()
starter.tweet_at_provider()
