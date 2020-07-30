import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys

def main():

    chrome_options = Options()

    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    base_url = "https://www.blowoutshop.de/raffle"
    driver.get(base_url)

    time.sleep(10)

    # auth_proxy(driver, USER, PASS)

    with open("autofill.yaml", 'r') as file:
        autofill_props = yaml.safe_load(file)

    complete_form(driver, autofill_props)


def complete_form(driver, properties):

    xpaths = properties.get("xpaths")
    textbox_xpaths = xpaths.get("textbox")
    dd_xpaths = xpaths.get("dropdown")
    inputs = properties.get("input")

    for key in textbox_xpaths.keys():
        xpath = textbox_xpaths[key]
        fill_input(driver, xpath, inputs.get(key))

    for key in dd_xpaths.keys():
        xpath = dd_xpaths[key]
        set_dropdown(driver, xpath, inputs.get(key))

    checkbox = driver.find_element_by_xpath(xpaths.get("checkbox"))
    checkbox.click()

    time.sleep(100)


def fill_input(driver, xpath, text):
    element = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].value = arguments[1];", element, text)


def set_dropdown(driver, xpath, option):
    dd = Select(driver.find_element_by_xpath(xpath))
    dd.select_by_visible_text(option)


def auth_proxy(driver, USER, PASS):
    time.sleep(5)
    driver.send_keys(USER)
    driver.send_keys(Keys.TAB)


if __name__ == '__main__':
    main()
