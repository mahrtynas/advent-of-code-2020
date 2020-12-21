import re
from functools import reduce


def extract_line_info(line):
    i, a = line.split("(contains")
    ingredients = re.findall("(\\w+)", i)
    allergens = re.findall("(\\w+)", a)
    return set(ingredients), set(allergens)

def simplify_list(unstable):
    stable = dict()
    alle = set()
    while unstable:
        unstable_copy = unstable.copy()
        for key, value in unstable_copy.items():
            unstable[key] = value.difference(alle)
            if len(unstable[key]) == 1:
                v = unstable.pop(key)
                stable[key] = v
                alle = alle.union(v)
    return stable

def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    foods = []
    for line in lines:
        food_ingredients, food_allergens = extract_line_info(line)
        foods.append({
            "ingredients": food_ingredients,
            "allergens":   food_allergens
            })
    ingredients = reduce(lambda a, b: a.union(b), [x["ingredients"] for x in foods])
    allergens = reduce(lambda a, b: a.union(b), [x["allergens"] for x in foods])
    res = {}
    for a in allergens:
        ing = set()
        for food in foods:
            if a in food["allergens"]:
                if not ing:
                    ing = food["ingredients"]
                else:
                    ing = ing.intersection(food["ingredients"])
        res[a] = ing
    ll = simplify_list(res)
    ks = [_ for _ in ll.keys()]
    ks.sort()
    ings = [ll[x].pop() for x in ks]
    print("CDIL: %s" % (",".join(ings)))




if __name__ == "__main__":
    main()
