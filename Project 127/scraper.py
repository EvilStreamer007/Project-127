from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/LENOVO/Desktop/Whitehat Jr/Projects/Project 127/chromedriver_win32/chromedriver.exe") 
browser.get(start_url) #opens url to scrape data
time.sleep(10)

scraped_data = []


def scrape():
        
    soup = BeautifulSoup(browser.page_source, "html.parser")

    brightstar_table = soup.find("table", attrs={"class", "wikitable"})
    
    tableBody = brightstar_table.find('tbody')

    tableRows = tableBody.find_all('tr')

    for row in tableRows:
        tableCols = row.find_all('td')
        print(tableCols)
            
        temp_list = []

        for colData in tableCols:
            data = colData.text.strip()
            temp_list.append(data)
            scraped_data.append(temp_list)
   
scrape()


starData = []

for i in range(0,len(scraped_data)):
    
    StarNames = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [StarNames, Distance, Mass, Radius, Lum]
    starData.append(required_data)

print(starData)


# Define Header
headers = ['Star_name','Distance','Mass','Radius','Luminosity']  

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(starData, columns=headers)

#Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")