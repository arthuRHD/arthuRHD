from datetime import datetime


class Human:

    def __init__(self):
        self.first_name = "Arthur"
        self.last_name = "Richard"
        self.gender = 'M'
        self.mail = "arthur.richard@protonmail.com"
        self.birth_date = datetime(year=1999, month=10, day=22)
        self.hobbies = {
            "sports": [
                "running",
                "climbing",
                "foot"
            ],
            "food": [
                "japanese",
                "french",
                "italian"
            ]
        }
        self.fields = ["programming", "electronics", "maths"]
        self.perks = ["problem solving", "listening"]
        self.wallet_addr = "0x16845Afbaf8320900d4aeE7CE11230a657A0C2f7"

    def __str__(self):
        print(self.first_name + self.last_name)

    @property
    def dream_car(self):
        with open('dream_car.stl', 'r') as dream_car_3d_vizualisation:
            return dream_car_3d_vizualisation.read()