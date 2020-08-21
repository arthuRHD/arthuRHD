from datetime import datetime


class Human:

    def __init__(self):
        first_name = "Arthur"
        last_name = "Richard"
        gender = 'M'
        mail = "arthur.richard@protonmail.com"
        birth_date = datetime(year=1999, month=10, day=22)
        hobbies = {
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
        fields = ["programming", "electronics", "maths"]
        qualities = ["problem solving", "listening"]
        flaws = ["FOMO", "tiktoking"]
        wallet_addr = "0x16845Afbaf8320900d4aeE7CE11230a657A0C2f7"

    def __str__(self):
        print(first_name + last_name)
