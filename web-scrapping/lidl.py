import requests
from bs4 import BeautifulSoup
import json
import os


def show_results(page) -> None:
    soup = BeautifulSoup(page.content, "html.parser")
    container = soup.find(id="s-results")

    products = container.find_all("li", class_="s-grid__item")
    
    all_data=[]
    for product in products:
        element = product.find('div', attrs={'data-grid-data': True})

        json_data = element['data-grid-data']       
        data = json.loads(json_data)


        current_price = data.get("price", {}).get("price", "")
        selected_data = {
            "fullTitle": data.get("fullTitle", ""),
            "productId": data.get("productId", ""),
            "price": current_price,
        }

        all_data.append(selected_data)

    with open('data.json', 'w') as f:
        json.dump(all_data, f, indent=4)
        print("Successfully saved data to data.json")
        


if __name__ == "__main__":
    URL = os.environ.get("URL")
    page = requests.get(URL)
    show_results(page)