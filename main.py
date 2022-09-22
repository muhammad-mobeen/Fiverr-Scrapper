# from selenium import webdriver
from click import command
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #..............
from selenium.webdriver.support import expected_conditions as EC    #................
from bs4 import BeautifulSoup
import xlsxwriter
import time
# from selenium.webdriver.common.proxy import Proxy, ProxyType  #.................
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from msvcrt import getche, getch
import os

WEBSITE = "https://www.fiverr.com"
PROXY = "149.14.242.250:9999"

class HQ:
    def __init__(self):
        hehehe_element = 999

    def commander(self):
        niche_list = self.scrape_niches()
        niche_tree_list = []
        for niche in niche_list:
            niche_items = self.scrape_niche_items(niche)
            niche_dict_list = []
            for i, item in enumerate(niche_items, 1):
                niche_dict_list.append(self.deep_scrape(item))
                print("Niche item #", i)
            # self.forge_excel({"niche": niche[0], "niche_item_list": niche_dict_list})
            niche_tree_list.append({"niche": niche[0], "niche_item_list": niche_dict_list})

        print("\n\n\nKarnamy strats here no go are no entrance hahahahaahaha!!\n\n")
        # print("niche_tree_list length: ", len(niche_tree_list))
        # print("Niche: ", niche_tree_list[0]["niche"])
        # print("Services: ", niche_tree_list[0]["niche_item_list"][0]["services_amt"])
        # print("Total Listings: ", niche_tree_list[0]["niche_item_list"][0]["listing_amt"])
        # print("\nTotal Cards: ", len(niche_tree_list[0]["niche_item_list"][0]["cards_list"]))
        # print("\nFirst Card:-\n")
        # print("Seller: ", niche_tree_list[0]["niche_item_list"][0]["cards_list"][0]["seller"])
        # print("Title: ", niche_tree_list[0]["niche_item_list"][0]["cards_list"][0]["title"])
        # print("Stars: ", niche_tree_list[0]["niche_item_list"][0]["cards_list"][0]["stars"])
        # print("Price: ", niche_tree_list[0]["niche_item_list"][0]["cards_list"][0]["price"])

        for niche_dict in niche_tree_list:
            self.forge_excel(niche_dict)
        return



    def gen_driver(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.headless = True
        chrome_options.add_argument('--proxy-server=http://'+PROXY)
        driver = uc.Chrome(options=chrome_options)
        return driver

    def assasin(self, source):
        soup = BeautifulSoup(source, "html.parser")
        is_sabotaged = soup.find(text="Please check the box below to access the site")
        if is_sabotaged:
            print("You are Bricked!")
            return True
        else:
            print("You are not bricked!")
            return False

    def driver_manager(self, urlink):
        while True:
            driver = self.gen_driver()
            driver.get(urlink)
            # time.sleep(3)
            if not self.assasin(driver.page_source):
                return driver
            driver.quit()

    
    def scrape_niches(self):
        driver = self.driver_manager(WEBSITE)

        explore_list_tuple = driver.find_elements(By.CSS_SELECTOR, '#__ZONE__main > div > div > div.main-categories.lohp-row.max-width-container > ul > li > a')
        explore_list_tuple_v2 = []
        for i, li_item in enumerate(explore_list_tuple,1):
            print("{}. Title: {}\n   Link: {}".format(i, li_item.text, li_item.get_attribute('href')))
            explore_list_tuple_v2.append((li_item.text, li_item.get_attribute('href')))

        driver.quit()
        return explore_list_tuple_v2


    def scrape_niche_items(self, explore_list_tuple):
        # driver = self.gen_driver()
        # driver.get(explore_list_tuple[0][1])
        driver = self.driver_manager(explore_list_tuple[1])
        # time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__ZONE__main > div > div > div.UsV1pzf.carousel-section > div > div.slides-list > div > div:nth-child(3) > a')))
        # with open(driver.page_source, "r") as f:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        popular_atag_list = soup.find_all("a", class_="most-popular-slide")
        popular_text_list = soup.find_all("span", class_="tbody-5 text-semi-bold m-r-12")
        print('\n\nMost Popular in {}\n'.format(explore_list_tuple[0]))

        popular_list = []
        for i, item in enumerate(popular_text_list,1):
            print("{}. Title: {}\n   Link: {}".format(i, item.text, WEBSITE + popular_atag_list[i-1].get('href')))
            popular_list.append((item.text, WEBSITE + popular_atag_list[i-1].get('href')))

        # self.assasin(driver.page_source)
        # os.system("pause")
        driver.quit()
        return popular_list
        # self.deep_scrape(popular_list)
        # parent = text[0].parent
        # print(parent)
        # spec = text[0].find_all(text="")
        # print(len(text))
        # print(text)
        # popular_list = doc.find_all('a', {'class': 'slide'})
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__ZONE__main"]/div/div/div[2]/div/div[2]/div/div[8]')))
        # os.system('pause')
        # print('wait is over now')
        # print(len(text))
        # popular_list = driver.find_elements(By.CSS_SELECTOR, '#__ZONE__main > div > div > div.UsV1pzf.carousel-section > div > div.slides-list > div > div:nth-child(3) > a')
        # /html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[6]/a
        # #__ZONE__main > div > div > div.UsV1pzf.carousel-section > div > div.slides-list > div > div:nth-child(9) > a
        # //*[@id="__ZONE__main"]/div/div/div[2]/div/div[2]/div/div[8]
        # //*[@id="__ZONE__main"]/div/div/div[2]/div/div[2]/div/div[1]
        # print(len(popular_list))
        # print("lol xddddddddddddddddddddddddd")
        # for items in text:
            # print(items.string)
            # print(items.text)
            # print(items.get_attribute('href'))



    def deep_scrape(self, popular_tuple):
        # driver = self.gen_driver()
        # driver.get(popular_tuple[0][1])
        driver = self.driver_manager(popular_tuple[1])
        # os.system("pause")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        services_amt = soup.find("span", class_="m-r-4")
        # print(services_amt)

        print(services_amt.text)

        cards_list = soup.find_all("div", class_="gig-card-layout")
        seller_name = (cards_list[0].find("div", class_="seller-name")).text
        seller_title = (cards_list[0].find("h3")).text
        rating_body = cards_list[0].find("span", class_="gig-rating text-body-2")
        seller_stars = rating_body.text
        seller_price = "Starting at " + ((cards_list[0].find("a", class_="price")).find("span")).text
        print("\nTotal Listings: ", len(cards_list))
        print("Seller: ",seller_name)
        print("Title: ",seller_title)
        print("Stars: ",seller_stars)
        print("Price: ",seller_price)

        niche_item_dict = {
            "niche_item": popular_tuple[0],
            "services_amt": services_amt.text,
            "listing_amt": len(cards_list),
            "cards_list": [{
                "seller": (card.find("div", class_="seller-name")).text,
                "title": (card.find("h3")).text,
                "stars": (card.find("span", class_="gig-rating text-body-2")).text,
                "price": "Starting at " + ((card.find("a", class_="price")).find("span")).text
                } for card in cards_list[:5]]
            }

        # self.assasin(driver.page_source)
        # os.system("pause")
        driver.quit()
        return niche_item_dict


    def forge_excel(self, niche_dict):        
        workbook = xlsxwriter.Workbook(niche_dict["niche"] + '.xlsx')
        bold_format = workbook.add_format()
        bold_format.set_bold()
        bold_yellow_cell = workbook.add_format()
        bold_yellow_cell.set_bg_color('yellow')
        bold_yellow_cell.set_bold()
        for niche_item_dict in niche_dict["niche_item_list"]:
            if len(niche_item_dict["niche_item"]) > 31:
                worksheet_name = niche_item_dict["niche_item"][:31]
            else:
                worksheet_name = niche_item_dict["niche_item"]
            worksheet = workbook.add_worksheet(worksheet_name)

            worksheet.write(0, 0, "Niche Title:", bold_format)
            worksheet.write(0, 1, niche_dict["niche"])

            worksheet.write(2, 0, "Popular Item in Niche:", bold_format)
            worksheet.write(2, 1, niche_item_dict["niche_item"])

            worksheet.write(4, 0, "Total Services:", bold_format)
            worksheet.write(4, 1, niche_item_dict["services_amt"])

            worksheet.write(6, 0, "Total Gigs Available:", bold_format)
            worksheet.write(6, 1, niche_item_dict["listing_amt"])

            worksheet.write(8, 0, "Top 5 Seller Data:-", bold_format)
            
            worksheet.write(9, 0, "Gig No.", bold_yellow_cell)
            worksheet.write(9, 1, "Seller Name", bold_yellow_cell)
            worksheet.write(9, 2, "Gig Title", bold_yellow_cell)
            worksheet.write(9, 3, "Stars", bold_yellow_cell)
            worksheet.write(9, 4, "Price", bold_yellow_cell)
            row = 10
            for i, card in enumerate(niche_item_dict["cards_list"], 1):
                worksheet.write(row, 0, "{}.".format(i))
                worksheet.write(row, 1, card["seller"])
                worksheet.write(row, 2, card["title"])
                worksheet.write(row, 3, card["stars"])
                worksheet.write(row, 4, card["price"])
                row+=1

                
        
        # Write on excel file
        # for i, t_data in enumerate(scrapped_data[1:], 0):
        #     worksheet.write(i, 0, str(t_data[0]))
        #     worksheet.write(i, 1, str(t_data[1]))

        try:
            workbook.close()    #Close the excel file and save it
            print("Successfully scrapped data to excel file!")
        except:
            print("Error: Could not save excel file!")



if __name__ == '__main__':

    # change 'ip:port' with your proxy's ip and port
    # proxy_ip_port = '202.44.196.170:8080'

    # proxy = Proxy()
    # proxy.proxy_type = ProxyType.MANUAL
    # proxy.http_proxy = proxy_ip_port
    # proxy.ssl_proxy = proxy_ip_port

    # capabilities = webdriver.DesiredCapabilities.CHROME
    # proxy.add_to_capabilities(capabilities)
    

# 'proxy-server=203.192.217.11:8080'
    # chrome_options = Options()
    # chrome_options = uc.ChromeOptions()
    # chrome_options.headless = False
    # chrome_options.add_argument('--proxy-server=http://'+PROXY)
    start_time = time.time()
    snister = HQ()
    snister.commander()
    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))
    print("Program took: {} minutes".format(end_time/60))

    # driver = uc.Chrome(options=chrome_options)...............................
    # driver.get("https://www.fiverr.com/")

    # driver = uc.Chrome(options=chrome_options)
    # driver.get('https://www.fiverr.com/')
    # driver.get(WEBSITE)................................................


    # os.system('pause')
    # explore_list_tuple = driver.find_elements(By.CSS_SELECTOR, '#__ZONE__main > div > div > div.main-categories.lohp-row.max-width-container > ul > li > a')
    # scroll = ActionChains(driver)
    # scroll.move_to_element(explore_list_tuple[0]).perform()
    #__ZONE__main > div > div > div.main-categories.lohp-row.max-width-container > ul > li:nth-child(2) > a
    # explore_list_tuple_v2 = []
    # for i, li_item in enumerate(explore_list_tuple,1):
    #     print("{}. Title: {}\n   Link: {}".format(i, li_item.text, li_item.get_attribute('href')))
    #     explore_list_tuple_v2.append((li_item.text, li_item.get_attribute('href')))

    
    # scrape_niche_items(explore_list_tuple_v2[0])

    # os.system('pause')
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[5]/ul/li[1]/a')
    # print(element.get_attribute('href'))
    # print(element.text)