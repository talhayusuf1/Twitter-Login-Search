from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = ""
password = ""


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option(
            'prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(
            'chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(3)

        usernameInput = self.browser.find_element(
            By.NAME, "text")
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)
        passwordInput = self.browser.find_element(
            By.NAME, "password")
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def search(self, hashtag):
        searchInput = self.browser.find_element(
            By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)

        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        list = self.browser.find_elements(
            By.XPATH, "//div[@data-testid='cellInnerDiv']/div[0]/div[0]/div[0]")
        for item in list:
            print(item.text)


twitter = Twitter(username, password)

twitter.signIn()
twitter.search("python")
