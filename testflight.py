from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

months = []
max_price = 150
fly_country = ["Francja", "Włochy"]#, "Hiszpania", "Portugalia", "Gruzja", "Malta", "Ukraina", "Grecja", "Izrael", "Turcja"]
esky = "https://www.esky.pl/okazje"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
chrome_path = "D:\studia\mojeprojekty\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_path, options=options)
time.sleep(0.1)


def FromAndTo():
    browser.get(esky)
    time.sleep(0.3)




    #sortowanie:







#na jakis miesiac, ile dni













    # the_best_departure = browser.find_element_by_xpath('//div[@class="cell-day number offer best"]')
    # the_best_departure_price = the_best_departure.find_element_by_xpath('//span[@class="price-wrapper"]/span')
    # print("The best price is: ", the_best_departure_price, "i ", the_best_departure_price)


    #other_departures = browser.find_elements_by_xpath('//div[@class=""]') #inneoferty




