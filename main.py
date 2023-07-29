import requests
import bs4
import re
import pandas

final = []
page = "https://www.ss.lv/lv/transport/cars/electric-cars/"
page_cont = requests.get(page)
page_html = bs4.BeautifulSoup(page_cont.content, 'html.parser')

for row_text in page_html.find_all('tr', id=re.compile("tr_")):
  result = str(row_text)
  x = result.find("msga2-o pp6")
  y = result.find(">", x + 1)
  z = result.find("<", y + 1)
  car_model = result[y + 1:z]
  x = result.find("msga2-o pp6", x + 1)
  y = result.find(">", x + 1)
  z = result.find("<", y + 1)
  car_year = result[y + 1:z]
  x = result.find("msga2-o pp6", x + 1)
  y = result.find(">", x + 1)
  z = result.find("<", y + 1)
  car_price = result[y + 1:z]
  car_price = car_price.replace(",", "")
  car_price = car_price.replace("  €", "")
  if (car_model != ""):
    final.append([car_model, car_year, car_price])

print(final)
df = pandas.DataFrame(final, columns=["name", "year", "price"])
df.to_csv('output.csv', index=False)

