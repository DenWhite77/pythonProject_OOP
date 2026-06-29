from src.product import load_data_from_json

categories = load_data_from_json('products.json')

for cat in categories:
    print(cat)
    for prod in cat.products:
        print(f"  {prod}")
    print()
