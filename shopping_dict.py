shopping_dict = {
    "warzywniak": ["marchew", "rukola", "seler"],
    "piekarnia": ["pączek", "bułki", "chleb"]
}
for k, v in shopping_dict.items():
    v_c = [item.capitalize() for item in v]
    print(f"Idę do {k.capitalize()} i kupię tam {v_c}")
list = shopping_dict.get("warzywniak") + shopping_dict.get("piekarnia")
no_of_items = len(list)
print(f'W sumie kupię {no_of_items} produktów.')
print("I to by było na tyle")
