import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time


def main():

    chrome_options = Options()

    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    base_url = "https://thenextdoor.fr/pages/stussy-x-nike-kukini"
    driver.get(base_url)


    with open("autofill.yaml", 'r') as file:
        autofill_props = yaml.safe_load(file)

    complete_form(driver, autofill_props)

    time.sleep(8)

    submit = driver.find_element_by_xpath('//*[@id="mc-embedded-subscribe"]')
    submit.click()


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


def fill_input(driver, xpath, text):
    element = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].value = arguments[1];", element, text)


def set_dropdown(driver, xpath, option):
    dd = Select(driver.find_element_by_xpath(xpath))
    dd.select_by_visible_text(option)


if __name__ == '__main__':
    main()
