from time import sleep
from Game import Game, Player
from Card import Card


# массив для хранения обьектов карт
cards = [Card(0, "", "Старт", 0, []),
         Card(1, "Коричневая", "Житная", 50, [50, 100, 150, 200]),
         Card(2, "Коричневая", "Нагатинская", 50, [50, 100, 150, 200]),
         Card(3, "", "Поезд", 0, []),
         Card(4, "Голубая", "Варшавское шоссэ", 100, [100, 150, 200, 400]),
         Card(5, "Голубая", "Огарево", 100, [100, 150, 200, 400]),
         Card(6, "Розовая", "Рязанский проспект", 150, [150, 200, 300, 600]),
         Card(7, "Розовая", "Ростовская набережная", 150, [150, 200, 300, 600]),
         Card(8, "", "Поезд", 0, []),
         Card(9, "Ораньжевая", "Полянка", 200, [200, 250, 400, 800]),
         Card(10, "Ораньжевая", "Рублевское шоссе", 200, [200, 250, 400, 800]),
         Card(11, "Красная", "Тверская", 250, [250, 300, 500, 1000]),
         Card(12, "Красная", "Пушкенская", 250, [250, 300, 500, 1000]),
         Card(13, "", "Поезд", 0, []),
         Card(14, "Желтая", "Грузинский вал", 300, [300, 350, 600, 1200]),
         Card(15, "Желтая", "Смоленская прощадь", 300, [300, 350, 600, 1200]),
         Card(16, "Зеленая", "Щусева", 350, [350, 400, 700, 1400]),
         Card(17, "Зеленая", "Кутузовский проспект", 350, [350, 400, 700, 1400]),
         Card(18, "", "Поезд", 0, []),
         Card(19, "Синяя", "Малая Бронная", 400, [400, 450, 800, 1600]),
         Card(20, "Синяя", "Столешнеков", 400, [400, 450, 800, 1600])]

players = Game()
players.start_game()

# инициализация переменной хранящей id игрока совершающего ход
id = 0

while True:
    rybik = players.next_move(id)
    players[id].cheng_position(rybik, len(cards)-1) # изминение позиции игрока
    house = cards[players[id].position] # на какой позиции/карте находится игрок
    print(f"карта -> {house.name}") # вывод названия карты на которой находится игрок
    # проверяем если карта не чья и это не ячейка старт то карту можно попытаться купить
    if house.name not in ("Старт", "Поезд"):
        if house.owner == None and players[id].balance >= house.price:
            while True:
                bay = input(f'Вы хотите купить {house.name} цена: {house.price} y/n: ')
                if bay.lower() == 'y':
                    players[id].cheng_balance(-house.price)
                    house.by_card(players[id].id)
                    print(f'игрок {players[id].name} купил {house.name} на балансе {players[id].balance}')
                    print(house)
                    break
                elif bay.lower() == 'n':
                    break
                else:
                    print('Введите на английском y или n')
        # если карта пренадлежит текущему игроку, то выводится информация о карте
        elif house.owner == players[id].id:
            print(house)
        # если карта пренадлежит другому игроку
        else:
            print(f"Оплата ренты в пользу {players[house.owner].name}")
            # оплата ренты
            players[id].cheng_balance(-house.get_rent())
            # перевод ренты владельцу карты
            players[house.owner].cheng_balance(house.get_rent())
            #  изминение уровня ренты карты
            house.get_rent()
            # если баланс текущего игрока = 0 то игра оконченна
            if players[id].balance <= 0:
                players.winner()
                print(f"ИГРА ОКОНЧЕНА!!! Игрок {players[id].name} БАНКРОТ")
                exit()
    elif house.name == "Поезд":
        print(f'Вы попали на клетку {house.name} ваы можете переместиться на любую клетку поля'
              f' стоимость перемещения 100')
        if players[id].balance >= 100:
            while True:
                trein = input(f'Вы хотите переместиться на другую клетку ваш баланс: {players[id].balance} y/n: ')
                if trein.lower() == 'y':
                    try:
                        new_cel = int(input(f"Введите номер клетки от 0 до {len(cards)-1}: "))
                    except ValueError:
                        print(f"необходимо ввести число от 0 до {len(cards)-1}")
                        continue
                    if new_cel >= 2 and new_cel <= len(cards):
                        players[id].teleport(new_cel)
                        # проверить если клетка чьято то предложить купить или платить ренту
                        new_house = cards[players[id].position]
                        if new_house.owner == None and new_house.name not in ("Старт", "Поезд")\
                                and players[id].balance >= new_house.price:
                            while True:
                                bay = input(f'Вы хотите купить {new_house.name} цена: {new_house.price} y/n: ')
                                if bay.lower() == 'y':
                                    players[id].cheng_balance(-new_house.price)
                                    new_house.by_card(players[id].id)
                                    print(f'игрок {players[id].name} купил {new_house.name} на балансе {players[id].balance}')
                                    print(new_house)
                                    break
                                elif bay.lower() == 'n':
                                    break
                                else:
                                    print('Введите на английском y или n')
                        elif new_house.owner == players[id].id:
                            print("Данная карта ваша")
                        elif new_house.name in ("Старт", "Поезд"):
                            print(f"Вы попали на клетку: {new_house.name}")
                        else:
                            print(f"Оплата ренты в пользу {players[new_house.owner].name}")
                            # оплата ренты
                            players[id].cheng_balance(-new_house.get_rent())
                            # перевод ренты владельцу карты
                            players[new_house.owner].cheng_balance(new_house.get_rent())
                            #  изминение уровня ренты карты
                            new_house.get_rent()
                            # если баланс текущего игрока = 0 то игра оконченна
                            if players[id].balance <= 0:
                                players.winner()
                                print(f"ИГРА ОКОНЧЕНА!!! Игрок {players[id].name} БАНКРОТ")
                                exit()
                        break
                    break
                elif trein.lower() == 'n':
                    break
                else:
                    print('Введите на английском y или n')
    # вычисление следующего игрока
    _, id = divmod(id + 1, len(players))
    sleep(3)