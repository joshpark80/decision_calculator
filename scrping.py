from bs4 import BeautifulSoup
import requests 

response = requests.get("https://www.finda.co.kr/savings/p2p-investments")
soup = BeautifulSoup(response.text, "html.parser")

rates = soup.find_all('li', 'h3', 'span')

for rate in rates:
	print(rate.get_text())