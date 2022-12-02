*4. Дан CSV файл с данными о товарах (article, title, description, price)
Необходимо считать файл, привести к списку словарей, выполнить
приведение типов значений атрибута price, провести валидацию данных
с помощью Pydantic, не верные записи вывести в другой файл, а из
списка удалить
from pydantic import BaseModel


class Product(BaseModel):
    article: str
    title: str
    description: str = ''
    price: float


with open('products.csv', 'r', encoding='utf-8') as file:
    headers = file.readline().strip().split(',')
    products = []
    invalid_product = []
    for product in file:
        values = product.strip().split(',')
        product = dict(list(zip(headers, values)))
        if not product['article']:
            invalid_product.append(product)
            continue
        try:
            product['price'] = float(product['price'])
        except ValueError:
            invalid_product.append(product)
            continue
        products.append(product)
with open('invalid_product.csv', 'w', encoding='utf-8') as file:
    headers = ','.join(headers)
    for product in invalid_product:
        values = ','.join(list(product.values()))
        headers += f'\n{values}'
    file.write(headers)

products = list(map(lambda x: Product(**x), products))
print(products)