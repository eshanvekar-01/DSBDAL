from bs4 import BeautifulSoup
import requests
import pandas as pd
webpage = requests.get('https://www.banggood.in/search/video-games.html?from=nav') 

sp = BeautifulSoup(webpage.content, 'html.parser')

# print(sp.text)

title = sp.find_all('a', 'title')
sellprice = sp.find_all('span', 'price')
origprice = sp.find_all('span', 'price-old-box')
review = sp.find_all('a', 'review')

titleloop = [titles.text for titles in title]
sellpriceloop = [sell.text for sell in sellprice]
origpriceloop = [orig.text for orig in origprice]
reviewloop = [reviews.text for reviews in review]

# print(titleloop)

data = {
    'Name_of_console':titleloop,
    'Selling_price':sellpriceloop,
    'Original_price':origpriceloop,
    'Number_of_reviews':reviewloop
}

print(len(titleloop))
print(len(sellpriceloop))
print(len(origpriceloop))
print(len(reviewloop))
df = pd.DataFrame(data, columns=[
    'Name_of_console',
    'Selling_price',
    'Original_price',
    'Number_of_reviews'
])

print(df)

df.to_excel(r'C:/Users/Disha Chavan/Desktop/Third year/SEM VI/DSBD/DSBDL/GroupC/Game_console3.xlsx', index=False)