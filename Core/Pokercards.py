import os
import random


class Pokercards:
    def __init__(self):
        # 扑克牌的数值字典
        self.poker_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "joker"]
        # 花色字典，其中红桃和方块为红色，草花黑桃为黑色
        self.poker_shapes = ["heart", "diamond", "spade", "club"]

    def random_card(self):
        value = random.choice(self.poker_values)
        shape = random.choice(self.poker_shapes)
        fshape = random.choice(self.poker_shapes)
        if value == "joker":
            if shape in ["heart", "diamond"]:
                fshape = "red"
            elif shape in ["spade", "club"]:
                fshape = "black"
        # 拼接文件路径
        card_file_name = f"./Statics/Pokercards/{fshape}_{value}.png"
        return {
            "value": value,
            "shape": shape,
            "file": card_file_name
        }


poker = Pokercards()
