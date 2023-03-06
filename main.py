from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import tools
import time
import openai

openai.api_key = "YOUR_API_KEY"

login = input("Login: ")
password = input("Password: ")
user = input("Who do you want to write?: ")

message = openai.Completion.create(model="text-davinci-003", prompt=f"Say hello to {user}")

options = Options()
options.add_argument("--window-size=1936,1056")

browser = webdriver.Chrome(options=options)
browser.get("http://instagram.com")
browser.implicitly_wait(5)

ig_cookie_block = browser.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']")
ig_cookie_block.click()
tools.wait()

browser.implicitly_wait(10)

fb_logging_button = browser.find_element(By.CLASS_NAME, "_ab37")
fb_logging_button.click()
tools.wait()


browser.implicitly_wait(10)

fb_cookie_block = browser.find_element(By.XPATH, "(//button[contains(@class,'_42ft _4jy0')])[2]")
fb_cookie_block.click()
tools.wait()

browser.implicitly_wait(10)

fb_login = browser.find_element(By.ID, "email")
fb_password = browser.find_element(By.ID, "pass")

browser.implicitly_wait(10)

fb_login.send_keys(login)
tools.wait()
fb_password.send_keys(password)
tools.wait()

browser.implicitly_wait(10)

login_button = browser.find_element(By.ID, "loginbutton")
login_button.click()
tools.wait()

browser.implicitly_wait(10)

ig_alert_block = browser.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']")
ig_alert_block.click()
tools.wait()

browser.implicitly_wait(10)

ig_alert_block = browser.find_element(By.XPATH, "(//div[contains(@class,'x9f619 x3nfvp2')])[2]")
ig_alert_block.click()
tools.wait()

browser.implicitly_wait(10)

ig_input = browser.find_element(By.XPATH, "//input[@class='_aauy focus-visible']")
ig_input.send_keys(user)
tools.wait()

ig_user = browser.find_element(By.XPATH, f"//a[@href='/{user}/']//div")
ig_user.click()
tools.wait()

click_send_message = browser.find_element(By.XPATH, "(//div[@role='button'])[2]")
click_send_message.click()
tools.wait()

send_message = browser.find_element(By.CLASS_NAME, "focus-visible")
send_message.send_keys(message.choices[0].text, Keys.ENTER)

time.sleep(100)