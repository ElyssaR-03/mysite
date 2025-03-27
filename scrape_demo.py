from bs4 import BeautifulSoup

with open('index.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

products = soup.find_all("div", class_="product")

for product in products:
    name = product.find("span", class_="name").text
    price = product.find("span", class_="price").text
    print(f"{name}: {price}")