INPUT = 'hepxcrrq'


class PasswordGenerator:
    def __init__(self, starting_password: str):
        self.password = starting_password

    def check_valid(self) -> bool:
        return self.includes_straight_of_three() and self.not_includes_i_o_l() and self.contains_two_nonoverlapping_pairs()

    def includes_straight_of_three(self) -> bool:
        for i in range(0, len(self.password)-2):
            if ord(self.password[i]) == ord(self.password[i+1]) - 1 and ord(self.password[i]) == ord(self.password[i+2]) - 2:
                return True
        return False

    def not_includes_i_o_l(self) -> bool:
        for c in self.password:
            if c in ['i', 'o', 'l']:
                return False
        return True

    def contains_two_nonoverlapping_pairs(self) -> bool:
        pair_count = 0
        index = 0
        while index < len(self.password) - 1:
            if self.password[index] == self.password[index+1]:
                pair_count += 1
                index += 2
            else:
                index += 1
        return pair_count >= 2

    def increment_password(self):
        new_password = ''
        carry_bit = 1
        for c in reversed(self.password):
            if ord(c) + carry_bit > 122:
                new_password += chr(ord(c) + carry_bit - 26)
                carry_bit = 1
            else:
                new_password += chr(ord(c) + carry_bit)
                carry_bit = 0

        self.password = ''.join(reversed(new_password))

    def increment_password_until_valid(self):
        self.increment_password()
        while not self.check_valid():
            self.increment_password()


def test_hijklmmn():
    pg = PasswordGenerator('hijklmmn')
    assert pg.includes_straight_of_three()
    assert not pg.not_includes_i_o_l()
    assert not pg.contains_two_nonoverlapping_pairs()
    assert not pg.check_valid()


def test_abbceffg():
    pg = PasswordGenerator('abbceffg')
    assert not pg.includes_straight_of_three()
    assert pg.not_includes_i_o_l()
    assert pg.contains_two_nonoverlapping_pairs()
    assert not pg.check_valid()


def test_abbcegjk():
    pg = PasswordGenerator('abbcegjk')
    assert not pg.includes_straight_of_three()
    assert pg.not_includes_i_o_l()
    assert not pg.contains_two_nonoverlapping_pairs()
    assert not pg.check_valid()


def test_next_pass_abcdefgh():
    pg = PasswordGenerator('abcdefgh')
    pg.increment_password_until_valid()
    assert pg.password == 'abcdffaa'


def test_next_pass_ghijklmn():
    pg = PasswordGenerator('ghijklmn')
    pg.increment_password_until_valid()
    assert pg.password == 'ghjaabcc'


pg = PasswordGenerator(INPUT)
pg.increment_password_until_valid()
print("Part 1: ", pg.password)
pg.increment_password_until_valid()
print("Part 2: ", pg.password)
