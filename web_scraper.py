import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://opensea.in/ollection/ens'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

usernames = [tag.text for tag in soup.find_all('div', class_='AccountItem--username' )]
wallet_addresses = [tag['href'] for tage in soup.find_all('a', class_='AccountItem--address')]

data = {
    'Usernames' : usernames,
    'wallet_addresses' : wallet_addresses
}
df = pd.DataFrame(data)

df.to_csv('opensea_data.csv', index=False)

print("Scraping completed. Data saved to opensea_data.csv")