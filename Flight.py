import time
from selenium import webdriver

def refreshpagewhenneeded(func,arg,browser):
    try:
        return func(arg)
        #print("SUccess")
    except:
        print("Refresh using")
        try:
            browser.refresh()
            time.sleep(3)
            func(arg)
        except:
            print("Failed")


class Flight:
    def __init__(self, browser, max_price):
        self.browser = browser
        self.max_price = max_price
        time.sleep(1)

    def get_amount_of_money_for_whole_flight(self):
        time.sleep(0.3)
        #price_two_ways = self.browser.find_element_by_xpath('//div[@class="aside aside-deals"]')
        price_two_ways = refreshpagewhenneeded(self.browser.find_element_by_xpath, '//div[@class="aside aside-deals"]', self.browser)
        print(price_two_ways.text.replace("\n",' '))
        #todo zapis do jakiegos excela

    def get_information_about_hours_of_flight(self):
        time.sleep(0.5)
        #hours_of_flights = self.browser.find_elements_by_xpath('//label[@class="leg selected with-facilities"]')
        hours_of_flights = refreshpagewhenneeded(self.browser.find_elements_by_xpath, '//label[@class="leg selected with-facilities"]',
                                               self.browser)
        for hours in hours_of_flights:
            print(hours.text.replace("\n",' ')) #ToDo Save to Excel or .txt or send to email
            break #todo not all only making condition


    def get_information_about_days_of_flights(self):
        time.sleep(0.3)
        #days_of_flights = self.browser.find_elements_by_xpath('//div[@class="title-wrap"]')
        days_of_flights = refreshpagewhenneeded(self.browser.find_elements_by_xpath, '//div[@class="title-wrap"]',
                                               self.browser)
        for days in days_of_flights:
            print(days.text.replace("\n",' ')) #ToDo Save to Excel or .txt or send to email
            break #todo not all only making condition

    def information_about_cheap_flights(self, days, month, link):
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(3)
        refreshpagewhenneeded(self.browser.get, link, self.browser)
        if days == 1:
            self.browser.find_element_by_xpath('//input[@id="radio-group-0-2"]').click()
        else:
            self.browser.find_element_by_xpath('//input[@id="radio-group-0-3"]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//span[@qa-month="' + str(month) + '"]').click()
        time.sleep(5)

        arrival_and_departure_info = self.browser.find_element_by_xpath('//h1[@class="h3"]').text
        # arrival_and_departure_info = refreshpagewhenneeded(self.browser.find_element_by_xpath, '//h1[@class="h3"]',self.browser)
        # print(arrival_and_departure_info)

        one_way_ticket_info_other = self.browser.find_elements_by_xpath('//div[@class="cell-day number offer"]')
        for other in one_way_ticket_info_other:
            self.browser.execute_script("arguments[0].scrollIntoView();", other)
            one_way_ticket_price = other.text.replace('\n', ' ').split(' ')[1]
            if (int(one_way_ticket_price) < self.max_price+ 50):
                other.click()
                time.sleep(1)
                print("----------------------------------------------------------------")
                self.get_information_about_days_of_flights()
                self.get_information_about_hours_of_flight()
                self.get_amount_of_money_for_whole_flight()

        #bestofall
        time.sleep(1)
        one_way_ticket_info = self.browser.find_element_by_xpath('//div[@class="cell-day number offer best"]')#or best selected ?
        self.browser.execute_script("arguments[0].scrollIntoView();", one_way_ticket_info)
        one_way_ticket_price = one_way_ticket_info.text.replace('\n',' ').split(' ')[1]
        if(int(one_way_ticket_price) < self.max_price + 100):

            one_way_ticket_info.click()
            print("----------------------------------------------------------------")
            time.sleep(1)
            self.get_information_about_hours_of_flight()
            self.get_amount_of_money_for_whole_flight()
            self.get_information_about_days_of_flights()
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(2)





# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# chrome_path = "D:\studia\mojeprojekty\chromedriver.exe"
# browser = webdriver.Chrome(executable_path=chrome_path, options=options)
#
# flight = Flight(browser, 150)
# flight.information_about_cheap_flights(1,6,"https://www.esky.pl/okazje/25989/KRK-TSF-FR")