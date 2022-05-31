# Password Generator

import random
import sys


class PasswordGenerator:

    def __init__(self):
        self._upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._lower_letters = self._upper_letters.lower()
        self._numbers = "0123456789"
        self._symbols = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
        self._all = "".join(self._upper_letters +
                            self._lower_letters + self._numbers + self._symbols)


    # takes the password length as an argument and generates random sequence of characters

    def random_generator(self, pass_length):
        self.pass_length = pass_length

        try:
            assert (int(self.pass_length) >= 4)
        except AssertionError as e:
            print("Either the input is not a number or it is less than 4.")
            sys.exit()

        generated_password = random.choices(self._all, k=self.pass_length)
        print("".join(generated_password))


    # takes four arguments to generate password that consists of specific characters

    def specific_generator(self, *, up, low, num, symb):
        self.up = up
        self.low = low
        self.num = num
        self.symb = symb

        try:
            assert ((int(self.up) + int(self.low) +
                     int(self.num) + int(self.symb)) >= 4)
        except AssertionError as e:
            print("Either the input is not a number or length is less than 4.")
            sys.exit()
        except ValueError as e:
            print("Either the input is not a number or length is less than 4.")
            sys.exit()

        random_up = random.choices(self._upper_letters, k=self.up)
        random_low = random.choices(self._lower_letters, k=self.low)
        random_num = random.choices(self._numbers, k=self.num)
        random_symb = random.choices(self._symbols, k=self.symb)
        all = "".join(random_up + random_low + random_num + random_symb)
        pass_length = self.up + self.low + self.num + self.symb
        generated_password = random.sample(list(all), k=pass_length)

        print("".join(generated_password))


    def validate(self, password):
        self.password = password
        _has_upper_letter = False
        _has_lower_letter = False
        _has_number = False
        _has_symbol = False

        try:
            assert len(self.password) > 0
        except AssertionError:
            print("Please, insert a password!")
            sys.exit()

        for char in list(self.password):
            if char.isupper():
                _has_upper_letter = True
            elif char.islower():
                _has_lower_letter = True
            elif char.isnumeric():
                _has_number = True
            elif char in self._symbols:
                _has_symbol = True

        missing_characters = []

        if _has_upper_letter != True:
            missing_characters.append("upper case letter")
        if _has_lower_letter != True:
            missing_characters.append("lower case letter")
        if _has_number != True:
            missing_characters.append("number")
        if _has_symbol != True:
            missing_characters.append("symbol")

        if len(missing_characters) == 0:
            print("Congratulations! Your password is secure!")
        else:
            print(
                f"Your password is missing the following characters: {missing_characters}")


pass_1 = PasswordGenerator()
# pass_1.random_generator(4)
# pass_1.specific_generator(up=4, low=2, num=2, symb=1)
# pass_1.validate("myP@ssword")
