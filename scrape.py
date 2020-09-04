import csv
import requests
from bs4 import BeautifulSoup


url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
soup = BeautifulSoup(html, "lxml")
table = soup.find('tbody', attrs={'class':'stripe'})

list_of_rows=[]
for row in table.findAll('tr'):
	list_of_cells=[]
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;', '')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

	
outfile = open("./inmates.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Last Name", "First Name","Middle Name", "Suffix", "Gender", "N/A", "Age", "City", "State"])
writer.writerows(list_of_rows)