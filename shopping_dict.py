shopping_dict = {
    "warzywniak": ["marchew", "rukola", "seler"],
    "piekarnia": ["pączek", "bułki", "chleb"],
    "ikea": ["hot-dog", "wieszaki","bambus"],
}
no_of_items = 0
for k, v in shopping_dict.items():
    no_of_items += len(v)
    v_c = [item.capitalize() for item in v]
    print(f"Idę do {k.capitalize()} i kupię tam {v_c}")

print(f'W sumie kupię {no_of_items} produktów.')
