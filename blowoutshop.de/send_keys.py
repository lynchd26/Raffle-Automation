import requests
import yaml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from time import sleep

def main():

    chrome_options = Options()

    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    base_url = "https://www.blowoutshop.de/raffle"
    driver.get(base_url)

    # variables
    first = 'Dara'
    last = 'Lynch'
    address = '37 Woodland Park, Rush'
    city = 'Dublin'
    country = 'Ireland'
    paypal = 'daralynch01@gmail.com'
    size = '42.5'
    instagram = 'lynch_dara'

    # Input & submit
    first_name = driver.find_element_by_xpath('//*[@id="vorname"]')
    first_name.send_keys(first)
    last_name = driver.find_element_by_xpath('//*[@id="nachname"]')
    last_name.send_keys(last)
    address_field = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div/div/div[1]/div[2]/div[2]/form/div/div[3]/input')
    address_field.send_keys(address)
    city_select = driver.find_element_by_xpath('//*[@id="Adresse"]')
    city_select.send_keys(city)
    country_select = Select(driver.find_element_by_xpath('//*[@id="Land"]'))
    country_select.select_by_visible_text(country)
    paypal_email = driver.find_element_by_xpath('//*[@id="email"]')
    paypal_email.send_keys(paypal)
    size_select = Select(driver.find_element_by_xpath('//*[@id="Groesse"]'))
    size_select.select_by_visible_text(size)
    instagram_user = driver.find_element_by_xpath('//*[@id="Insta"]')
    instagram_user.send_keys(instagram)
    pickup = Select(driver.find_element_by_xpath('//*[@id="Pickup"]'))
    pickup.select_by_visible_text('NO')
    checkbox = driver.find_element_by_xpath('//*[@id="privacy-checkbox"]')
    checkbox.click()
    submit = driver.find_element_by_xpath('//*[@id="support"]/div/div[12]/button')
    submit.click()
    sleep(120)

if __name__ == '__main__':
    main()