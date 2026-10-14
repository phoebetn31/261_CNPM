import json

def load_categories():
    with open("data/cate.json", encoding="utf-8") as f:
        return json.load(f)

def load_products():
    with open("data/products.json", encoding="utf-8") as f:
        prods = json.load(f)
        return prods

if __name__ == "__main__":
    print(load_products())