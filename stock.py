from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#Get stock ticker
stock = input("Enter stock ticker: ")

#create URL for stock ticker
url = 'https://finance.yahoo.com/quote/'+stock+'/financials'

#open webpage, store data beautiful soup
driver = webdriver.Chrome()
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)
data = []

#get data, store as list
a = soup.find_all('span')
counter = 0

#sort through data with loop, append text to 'data' array
for b in a:
    data.append(b.text)

'''search for total revenue, store data & years
years are static in data set, thus counter arithymatic > loop
revenue is static after searching for total revenue
also can search for: net income, cost of revenue, gross profit, etc.

'''
for b in data:
    if b == 'Total Revenue':
        revenue = data[counter+1:counter+6]
        year = data[counter-5:counter] 
    counter = counter+1

#convert data from list to dataframe with pandas
df = pd.DataFrame({'Year':year, 'Revenue':revenue})

#transpose data for conversion to excel
df2 = df.transpose()
#print data set to view/check data
print(df2)
#create csv file with data set
df2.to_csv('revenue.csv', header=False)
