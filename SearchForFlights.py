import time
from selenium import webdriver
import Flight


months = []
max_price = 300
#fly_country = ["Francja", "Włochy", "Hiszpania", "Portugalia", "Gruzja", "Malta", "Grecja", "Izrael", "Turcja"]
fly_country = ["Portugalia", "Hiszpania"]
esky = "https://www.esky.pl/okazje" #for polish platform #todo english
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
chrome_path = "D:\studia\mojeprojekty\chromedriver.exe"  #change executable path
browser = webdriver.Chrome(executable_path=chrome_path, options=options)
time.sleep(0.1)


class SearchForFlights:
    def __init__(self, arrival, departure):
        browser.get(esky)
        self.arrival = arrival
        self.departure = departure
        self.from_where = '//input[@class="input filter-input"]'
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[0])

    def fillfromandtoflightandsort(self):
        #FROM
        fly_from = browser.find_elements_by_xpath(self.from_where)[0]
        self.fillcountrynames(self.departure,fly_from)
        # TO:
        fly_to = browser.find_elements_by_xpath(self.from_where)[1]
        for country in self.arrival:
            self.fillcountrynames(country, fly_to)

        search_occassion = browser.find_element_by_xpath('//button[@class="search btn normal transaction"]')
        search_occassion.click()
        time.sleep(2)

        #SORTING
        sorting_price = browser.find_element_by_xpath('//div[@data-title="Sortuj po"]')
        # scroll
        browser.execute_script("arguments[0].scrollIntoView();", sorting_price)
        time.sleep(0.1)
        sorting_price.click()
        choosing_ascending_price = browser.find_element_by_xpath('//label[@for="DealsSorter_opt_Price-Ascending"]').click()

    def fillcountrynames(self, country, window):
        window.clear()
        time.sleep(0.2)
        window.send_keys(" " + country + "\n")
        time.sleep(0.2)

    def searchforflight(self,month, day_option):
        self.choosecheapflight(month, day_option)
        show_more_flights = browser.find_element_by_xpath('//div[@class = "show-more-deals"]')
        browser.execute_script("arguments[0].scrollIntoView();", show_more_flights)
        show_more_flights.click()

    def choosecheapflight(self,month, optionday ):
        dest_city = browser.find_elements_by_xpath('//a[@class="btn function link"]')
        dest_city_see_more = browser.find_elements_by_xpath('//a[@class="btn function see-more"]')  ##jeszcze nie zrobione

        for city in dest_city:
            min_price_per_2_way_fligh = int(city.get_attribute("data-qa-tile").split(';')[-2])
            time.sleep(0.1)
            if (min_price_per_2_way_fligh < max_price):
                path_to_go = city.get_attribute("href")
                print(path_to_go)
                flight = Flight.Flight(browser, max_price)
                flight.information_about_cheap_flights(optionday, month, path_to_go)
            else:
                break
        print("The End")

        #notdoneyet
        for city in dest_city_see_more:
            min_price_per_2_way_fligh = int(city.get_attribute("data-qa-tile").split(';')[-2])
            time.sleep(0.1)
            if (min_price_per_2_way_fligh < max_price):
                print(city.get_attribute("href"))
            else:
                break


sf = SearchForFlights(fly_country, "Kraków")
sf.fillfromandtoflightandsort()
sf.searchforflight(8, 2)

