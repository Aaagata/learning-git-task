shopping_dict = {
    "warzywniak": ["marchew", "rukola", "seler"],
    "piekarnia": ["pączek", "bułki", "chleb"]
}
for k, v in shopping_dict.items():
    print(f"Idę do {k} i kupię tam {v}")
list = shopping_dict.get("warzywniak") + shopping_dict.get("piekarnia")
no_of_items = len(list)
print(f'W sumie kupię {no_of_items} produktów.')
    