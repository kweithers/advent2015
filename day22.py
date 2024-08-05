PLAYER_HP = 50
PLAYER_MANA = 500
BOSS_HP = 55
BOSS_DAMAGE = 8


class Player:
    def __init__(self, hp: int, mana: int, armor: int = 0, armor_duration: int = 0, recharge_duration: int = 0) -> None:
        self.hp: int = hp
        self.mana: int = mana
        self.armor: int = armor
        self.armor_duration: int = armor_duration
        self.recharge_duration: int = recharge_duration


class Boss:
    def __init__(self, hp: int, damage: int, poison_duration: int = 0) -> None:
        self.hp = hp
        self.damage = damage
        self.poison_duration = poison_duration


class Battle:
    spells = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
    lowest_cost_victory = float('inf')
    mana_spent = 0

    def __init__(self, player: Player, boss: Boss, hard_mode: bool) -> None:
        self.player = player
        self.boss = boss
        self.hard_mode = hard_mode

    def check_winner(self) -> bool:
        if self.boss.hp <= 0:
            self.lowest_cost_victory = min(
                self.lowest_cost_victory, self.mana_spent)
            return True
        if self.player.hp <= 0:
            return True
        return False

    def dfs_battle(self) -> None:
        if self.mana_spent > self.lowest_cost_victory:
            return

        starting_player_stats = (self.player.hp, self.player.mana, self.player.armor,
                                 self.player.armor_duration, self.player.recharge_duration)
        starting_boss_stats = (
            self.boss.hp, self.boss.damage, self.boss.poison_duration)
        starting_mana = self.mana_spent

        for spell in self.spells:
            # reset boss and player and mana spent
            self.player = Player(*starting_player_stats)
            self.boss = Boss(*starting_boss_stats)
            self.mana_spent = starting_mana

            if self.hard_mode:
                self.player.hp -= 1
                if self.check_winner():
                    continue

            # player turn
            self.apply_effects()
            if self.check_winner():
                continue

            match spell:
                case "Magic Missile":
                    if self.player.mana < 53:
                        continue
                case "Drain":
                    if self.player.mana < 73:
                        continue
                case "Shield":
                    if self.player.armor_duration > 0 or self.player.mana < 113:
                        continue
                case "Poison":
                    if self.boss.poison_duration > 0 or self.player.mana < 173:
                        continue
                case "Recharge":
                    if self.player.recharge_duration > 0 or self.player.mana < 229:
                        continue

            self.player_turn(spell)
            if self.check_winner():
                continue

            # boss turn
            self.apply_effects()
            if self.check_winner():
                continue
            self.player.hp -= max(1, self.boss.damage - self.player.armor)
            if self.check_winner():
                continue

            self.dfs_battle()

    def apply_effects(self) -> None:
        if self.boss.poison_duration > 0:
            self.boss.hp -= 3
            self.boss.poison_duration -= 1

        if self.player.recharge_duration > 0:
            self.player.mana += 101
            self.player.recharge_duration -= 1

        if self.player.armor_duration > 0:
            self.player.armor = 7
            self.player.armor_duration -= 1
        else:
            self.player.armor = 0

    def player_turn(self, name: str) -> None:
        match name:
            case "Magic Missile":
                self.player.mana -= 53
                self.mana_spent += 53
                self.boss.hp -= 4
            case "Drain":
                self.player.mana -= 73
                self.mana_spent += 73
                self.boss.hp -= 2
                self.player.hp += 2
            case "Shield":
                self.player.mana -= 113
                self.mana_spent += 113
                self.player.armor_duration = 6
            case "Poison":
                self.player.mana -= 173
                self.mana_spent += 173
                self.boss.poison_duration = 6
            case "Recharge":
                self.player.mana -= 229
                self.mana_spent += 229
                self.player.recharge_duration = 5


p = Player(PLAYER_HP, PLAYER_MANA)
b = Boss(BOSS_HP, BOSS_DAMAGE)

bat = Battle(p, b, False)
bat.dfs_battle()
print("Part 1: ", bat.lowest_cost_victory)

bat = Battle(p, b, True)
bat.dfs_battle()
print("Part 2: ", bat.lowest_cost_victory)
