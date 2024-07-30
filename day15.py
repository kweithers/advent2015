from dataclasses import dataclass
N_INGREDIENTS = 100


@dataclass(frozen=True)
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


ingredients: dict[str, Ingredient] = {"Sugar": Ingredient("Sugar", 3, 0, 0, -3, 2), "Sprinkles": Ingredient("Sprinkles", -3, 3, 0, 0, 9),
                                      "Candy": Ingredient("Candy", -1, 0, 4, 0, 1), "Chocolate": Ingredient("Chocolate", 0, 0, -2, 2, 8)}

max_score = 0
max_score_500_calories = 0
for i in range(N_INGREDIENTS):
    for j in range(N_INGREDIENTS-i):
        for k in range(N_INGREDIENTS-i-j):
            l = N_INGREDIENTS-i-j-k

            capacity = i * ingredients["Sugar"].capacity + \
                j * ingredients["Sprinkles"].capacity + \
                k * ingredients["Candy"].capacity + \
                l * ingredients["Chocolate"].capacity

            durability = i * ingredients["Sugar"].durability + \
                j * ingredients["Sprinkles"].durability + \
                k * ingredients["Candy"].durability + \
                l * ingredients["Chocolate"].durability

            flavor = i * ingredients["Sugar"].flavor + \
                j * ingredients["Sprinkles"].flavor + \
                k * ingredients["Candy"].flavor + \
                l * ingredients["Chocolate"].flavor

            texture = i * ingredients["Sugar"].texture + \
                j * ingredients["Sprinkles"].texture + \
                k * ingredients["Candy"].texture + \
                l * ingredients["Chocolate"].texture

            calories = i * ingredients["Sugar"].calories + \
                j * ingredients["Sprinkles"].calories + \
                k * ingredients["Candy"].calories + \
                l * ingredients["Chocolate"].calories

            score = max(0, capacity) * max(0, durability) * \
                max(0, flavor) * max(0, texture)

            max_score = max(max_score, score)
            if calories == 500:
                max_score_500_calories = max(max_score_500_calories, score)


print("Part 1: ", max_score)
print("Part 2: ", max_score_500_calories)
