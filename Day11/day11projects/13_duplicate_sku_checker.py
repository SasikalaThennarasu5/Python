skus = ["SKU1", "SKU2", "SKU1", "SKU3"]
sku_set = set(skus)
duplicates = len(skus) != len(sku_set)

print("Has duplicates?", duplicates)