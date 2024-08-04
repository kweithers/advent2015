from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Item:
    name: str
    cost: int
    damage: int
    armor: int


class Player:
    def __init__(self, damage: int, armor: int, hp: int) -> None:
        self.damage: int = damage
        self.armor: int = armor
        self.hp: int = hp


class Battle:
    def __init__(self, player: Player, boss: Player) -> None:
        self.player = player
        self.boss = boss

    def player_wins(self) -> bool:
        while self.player.hp > 0 and self.boss.hp > 0:
            self.boss.hp -= max(1, self.player.damage - self.boss.armor)
            if self.boss.hp <= 0:
                return True
            self.player.hp -= max(1, self.boss.damage - self.player.armor)
        return self.boss.hp <= 0


weapons = set([Item("Dagger",  8, 4, 0), Item("Shortsword", 10, 5, 0), Item("Warhammer", 25, 6, 0),
              Item("Longsword", 40, 7, 0), Item("Greataxe", 74, 8, 0)])

armors = set([Item("Leather", 13, 0, 1), Item("Chainmail", 31, 0, 2), Item("Splintmail", 53, 0, 3),
             Item("Bandedmail", 75, 0, 4), Item("Platemail", 102, 0, 5)])

rings = set([Item("Damage +1", 25, 1, 0), Item("Damage +2", 50, 2, 0), Item("Damage +3", 100, 3, 0),
            Item("Defense +1", 20, 0, 1), Item("Defense +2", 40, 0, 2), Item("Defense +3", 80, 0, 3)])


lowest_cost_win = float('inf')
highest_cost_loss = float('-inf')
combos = ([w, a, r] for w in combinations(weapons, 1) for n_armor in [0, 1] for a in combinations(
    armors, n_armor) for n_rings in [0, 1, 2] for r in combinations(rings, n_rings))

for c in combos:
    player = Player(0, 0, 100)
    boss = Player(8, 2, 109)
    cost = 0

    for i in range(3):
        for item in c[i]:
            cost += item.cost
            player.armor += item.armor
            player.damage += item.damage

    b = Battle(player, boss)
    if b.player_wins():
        lowest_cost_win = min(lowest_cost_win, cost)
    else:
        highest_cost_loss = max(highest_cost_loss, cost)

print("Part 1: ", lowest_cost_win)
print("Part 2: ", highest_cost_loss)
