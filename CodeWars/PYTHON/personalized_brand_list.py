"""
    Assume you are creating a webshop and you would like to help the user in the search. You have products with brands,
    prices and name. You have the history of opened products (the most recently opened being the first item).

    Your task is to create a list of brands ordered by popularity, if two brands have the same popularity level
    then choose the one which was opened last from the two and second the other one.

    Product popularity is calculated from the history. If a product is more times in the history than it is more popular.
    Your function will have one parameter which will be always an array/list of object.
    example product: { name: "Phone", price: 25, brand: "Fake brand" }
"""

def sorted_brands(history):
    #6 kyu

    dct_brands: dict = dict()
    for brand in history:
        if brand.get("brand") not in dct_brands:
            dct_brands[brand.get("brand")] = 1
        else:
            dct_brands[brand.get("brand")] = dct_brands.get(brand.get("brand")) + 1
            
    if len(dct_brands) >= 1:
        dct_brands = sorted(dct_brands.items(), key=lambda dct: dct[-1], reverse=True)
        return [brand[0] for brand in dct_brands]
    else: return []