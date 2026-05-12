#import libraries and setup
from utils.driver import setup_driver
import time
import pandas as pd

WEBSITE_URL = "hhttps://www.landsearch.com/price"

# create a driver instance
driver = setup_driver()

# navigate to the website
driver.get(WEBSITE_URL)

# find each "State" row/element and extract the data
rows = driver.find_elements('xpath', "//tr[starts-with(@data-uid, 'price-')]")

# create lists to store the data
state=[]
avg_price=[]
avg_price_per_acre=[]
avg_acreage=[]
num_listings=[]

# loop through each row and extract the data
for row in rows:
    state.append(row.find_element('xpath', ".//th//a").text)
    avg_price.append(row.find_element('xpath', ".//td[1]").text)
    avg_price_per_acre.append(row.find_element('xpath', ".//td[2]").text)
    avg_acreage.append(row.find_element('xpath', ".//td[3]").text)
    num_listings.append(row.find_element('xpath', ".//td[4]").text)
    
# after scraping is complete, close the driver and quit
time.sleep(1)
driver.close()
driver.quit()

# create a dataframe to store the scraped data
landsearch_data = pd.DataFrame({
    "state": state,
    "avg_price": avg_price,
    "avg_price_per_acre": avg_price_per_acre,
    "avg_acreage": avg_acreage,
    "num_listings": num_listings
})

# print the dataframe
print(landsearch_data)

# save the dataframe to a csv file in the data folder with the current date in the filename
date = time.strftime("%Y-%m-%d")
landsearch_data.to_csv(f'/data/landsearch_data_{date}.csv', index=False)