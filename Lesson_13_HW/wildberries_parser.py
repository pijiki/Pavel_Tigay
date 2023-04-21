from config import *
from base_parser import BaseParser
from mixin import ProductDetailMixin
import time

from bs4 import BeautifulSoup


class CategoryParser(BaseParser, ProductDetailMixin):
    def __init__(self):
        super(CategoryParser, self).__init__()
        self.DATA = {}

    def category_block_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        category_links = soup.find_all('u1', class_='menu-catalog__list-2')
        for category in category_links:
            category_title = category.find('a', class_='j-menu-item').get_text(strip=True)
            print(Color.BLUE + category_title)
            self.DATA[category_title] = []
            category_link = self.host + category.get('href')
            print(category_link)
            category_page = self.get_html(category_link)
            self.category_page_parser(category_page, category_title)

    def category_page_parser(self, category_page, category_title):
        soup = BeautifulSoup(category_page, 'html.parser')
        section = soup.find('div', class_='catalog-start-content__main')
        section_catalog = section.find_all('div', class_='product-card-list')
        products = section_catalog.find_all('div', class_='product-card__main')
        for product in products[:3]:
            product_name = product.find('a', class_='product-name').get_text(strip=True)
            print(Color.YELLOW + product_name + Color.RESET)
            product_price = product.find('div', class_='f-16').get_text(strip=True)
            product_link = self.host + product.find('a', class_='product-link').get('href')
            product_detail_page = self.get_html(product_link)
            characteristics = self.get_detail_info(product_detail_page)
            self.DATA[category_title].append({
                'Имя продукта': product_name,
                'Цена продукта': product_price,
                'Ссылка на продукт': product_link,
                'Характеристики': characteristics
            })

        time.sleep(50)


def start_category_parsing():
    """Старт скрипта"""
    parser = CategoryParser()
    category = 'elektronika'
    category_link = 'https://uz.wildberries.ru/catalog/' + category

    html = parser.get_html(category_link)
    parser.category_block_parser(html)
    parser.save_data_to_json(category, parser.DATA)



start_category_parsing()
