def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices
products = ["apple", "banana", "orange", "apple", "grape", "apple"]
indices = linear_search_product(products, "apple")
print(indices)  # Output: [0, 3, 5]
