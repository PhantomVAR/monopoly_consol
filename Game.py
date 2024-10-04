import random
from Player import Player
from Decor import Decor


class Game:
    """класс Game инициирует начало игры """
    def __init__(self):
        self.player = []

    @Decor("=", 80, "WARNING")
    def start_game(self):
        """в данном методе происходит выбор количества играков
        и указание имен """
        count_players = 0
        # пользователь выбирает количество играков
        while True:
            try:
                count_players = int(input("введите количество игроков от 2 до 4 или 0 для завершения игры: "))
            except ValueError:
                print("необходимо ввести число от 2 до 4 или 0 для завершения игры")
                continue
            if count_players >= 2 and count_players <= 4:
                break
            elif count_players == 0:
                exit()

        # создание обьектов играков, пользователи задают имя
        for id_player in range(count_players):
            name_player = input(f"Игрок {id_player+1} введи свое имя: ")
            self.__add_player(id_player, name_player)

    @Decor("*", 80, "OKGREEN")
    def next_move(self, id: int):
        """возвращает результат броска кубиков"""
        cube = random.randint(1, 12)  # имитация выброса костей от 1 до 12
        print(f"ходит игрок {id+1} {self.__getitem__(id).name} баланс {self.__getitem__(id).balance} на кубике выпало {cube}")
        return cube

    def __add_player(self, id_player: int, name_player: str):
        self.player.append(Player(id_player, name_player))

    def __getitem__(self, index: int) -> Player:
        """возвращает обьект Player по индексу"""
        return self.player[index]

    def __len__(self):
        return len(self.player)

    @Decor("-!", 40, "OKCYAN")
    def winner(self):
        """данная функция возвращает игрока с наибольшим болансов на счету"""
        win = ""
        balance = 0
        for i in range(self.__len__()):
            if self.__getitem__(i).balance >= balance:
                balance = self.__getitem__(i).balance
                win += self.__getitem__(i).name + " "
        print(f"Победил игрок {win}  с балансом {balance}")
