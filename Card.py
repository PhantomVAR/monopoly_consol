class Card:
    """класс описывающий карты"""
    def __init__(self, id_card: int, street: str, name: str, price: int, rent):
        self.id_card = id_card
        self.street = street
        self.name = name
        self.owner = None
        self.price = price
        self.rent = rent
        self.level_rent = 1

    def by_card(self, player: int):
        """метод приобритения карты"""
        self.owner = player

    # def by_card_new(self, player: int):
    #     self.owner = player

    def set_rent(self):
        """метод повышения ренты карты, максимальный уровень 4"""
        if self.owner and self.level_rent < 4:
            self.level_rent += 1

    def get_rent(self):
        """"возвращает текущий уровень ренты"""
        return self.rent[self.level_rent-1]

    def __str__(self):
        """печатает в консоли всю информацию о карте на текущий момент
            Улица: Название: Хозяин: Стоимость: Рента: Уровень ренты:"""
        return (f"Улица: {self.street} Название: {self.name} Хозяин: игрок:"
                f"{self.owner+1} Стоимость: {self.price} Рента: {self.rent} Уровень ренты: {self.level_rent} ")

