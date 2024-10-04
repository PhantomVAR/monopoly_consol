from Card import Card

class Player:
    """класс игрок"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.balance = 1500
        self.position = 0

    def __divmod__(self, step, len_cards):
        return divmod(self.position + step, len_cards)

    def cheng_position(self, step: int, len_cards: int):
        """изминения позиции на доске
        в случаи проходжения полного круга начисляется 200 монет"""
        krug, self.position = self.__divmod__(step, len_cards)
        if krug != 0:
            self.cheng_balance(200)

    def teleport(self, step: int):
        """если попал на клетку поезд"""
        self.position = step
        self.cheng_balance(-100)

    def cheng_balance(self, value: int):
        """в данном классе происходит увеличиение баланса игрока на переданное значение"""
        self.balance += value