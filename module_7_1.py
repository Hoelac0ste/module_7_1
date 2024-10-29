from pprint import pprint

class Shop:
    file_name = 'products.txt'
    text = ''
    def get_products(self):
        with open(self.file_name) as file:
            self.text = file.read()
            pprint(self.text)
        return self.text
        file.close()

    def add(self, *products):
        for i in products:
            file = open(self.file_name)
            text = file.read()
            file.close()
            if i.name in text:
                print('Продукт уже есть в магазине')
            else:
                file = open(self.file_name, 'a')
                file.write(f'{i.name}, {i.weight}, {i.category}\n')
                print(f'Продукт {i.name} добавлен в магазин')
                file.close()

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

p1 = Product('Potato', 50.0, 'Vagetables')
p2 = Product('Tomato', 32.0, 'Vagetables')
p3 = Product('Orange', 78.0, 'Fruits')
print(p1)
s1 = Shop()
s1.add(p1, p2)
s1.add(p1, p2)

s1.get_products()
