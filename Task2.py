import csv
import timeit
from BTrees.OOBTree import OOBTree


def load_items(filename):
    items = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append({
                'ID': int(row['ID']),
                'Name': row['Name'],
                'Category': row['Category'],
                'Price': float(row['Price'])
            })
    return items

# Створення структур
items_tree = OOBTree()
items_dict = {}


# Функції для додавання товару в структуру
def add_item_to_tree(tree, item):
    tree[item['ID']] = item

def add_item_to_dict(dictionary, item):
    dictionary[item['ID']] = item


# Функції для діапазонного запиту
def range_query_tree(tree, min_price, max_price):
    results = []
    for key, value in tree.items(min_price, max_price):
        if min_price <= float(value['Price']) <= max_price:
            results.append(value)
    return results

def range_query_dict(dictionary, min_price, max_price):
    results = []
    for key in dictionary.keys():
        value = dictionary[key]
        if min_price <= float(value['Price']) <= max_price:
            results.append(value)
    return results



items = load_items('generated_items_data.csv')
min_price = 20
max_price = 400

for item in items:
    add_item_to_tree(items_tree, item)
    add_item_to_dict(items_dict, item)

# Вимірювання часу
tree_time = timeit.timeit(lambda: range_query_tree(items_tree, min_price, max_price), number=100)
dict_time = timeit.timeit(lambda: range_query_dict(items_dict, min_price, max_price), number=100)

print(f'Total range_query time for OOBTree: {tree_time:.6f} seconds')
print(f'Total range_query time for Dict: {dict_time:.6f} seconds')
