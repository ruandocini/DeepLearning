from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 

game_url = "chrome://dino"
chromebrowser_path = "/Users/cliente/Downloads/chromedriver"

chrome_options = Options()
chrome_options.add_argument("disable-infobars")

browser = webdriver.Chrome(executable_path = chromebrowser_path,chrome_options=chrome_options)
browser.get('chrome://dino')
browser.maximize_window()