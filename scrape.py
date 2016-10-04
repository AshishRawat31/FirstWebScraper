import csv
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
response = requests.get(url)
html=response.content

soup=BeautifulSoup(html, "html.parser") #It is very important to leave indentation between html, "html.parser"
Table=soup.find('table', class_='wikitable sortable plainrowheaders')

list_of_rows=[]
for row in Table.findAll('tr'):
    list_of_cells=[]
    for cell in row.findAll(['td','th']):
        if cell.find('th'):
            list_of_cells.append(text)
            break
        text=cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile=open("./inmates.csv", "w")
writer=csv.writer(outfile)
writer.writerows(list_of_rows)
outfile.close()