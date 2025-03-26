import random

mylist = ["kivi", "paber", "käärid"]
game = input("Kas soovite mängida mängu 'kivi, paber, käärid'? (Jah/Ei): ").strip().lower()
if game == 'jah':
    game_choice = input("Kas soovite mängida mängu 'inimese vs robot' või 'inimene vs inimene'? (robot/inimene): ").strip().lower()
    if game_choice == 'robot':
        # Игра между человеком и роботом
        player = input("Sisesta oma nimi: ")
        player_point = 0
        robot_point = 0

        while True:
            print("Olemasolevad valikud 1)kivi, 2)käärid, 3)paber")
            try:
                pvalik = int(input(f"Valige joonis 1, 2 või 3: "))
                if pvalik not in [1, 2, 3]:
                    print("Vale valik, proovige uuesti.")
                    continue
            except ValueError:
                print("Vale valik, proovige uuesti.")
                continue

            robot_choice = random.choice(mylist)
            if pvalik == 1:
                p = "kivi"
            elif pvalik == 2:
                p = "käärid"
            elif pvalik == 3:
                p = "paber"

            print(f"{player} - {p}, robot - {robot_choice}")

            if p == robot_choice:
                print("Tie")
            elif (p == "kivi" and robot_choice == "käärid") or (p == "käärid" and robot_choice == "paber") or (p == "paber" and robot_choice == "kivi"):
                print("Mängija võit")
                player_point += 1
            else:
                print("Roboti võit")
                robot_point += 1

            print(f"Skoor: {player} - {player_point}, robot - {robot_point}")

            # Выход из игры
            exit_game = input("Kas soovite mängu jätkata? (jah/ei): ").strip().lower()
            if exit_game != "jah":
                break
    elif game_choice == 'inimene':
        # Игра между двумя игроками
        player1 = input("Sisestage esimene mängija nimi: ")
        player2 = input("Sisestage teise mängija nimi: ")
        player1_point = 0
        player2_point = 0

        while True:
            print(f"{player1}, olemasolevad valikud 1)kivi, 2)käärid, 3)paber")
            try:
                p1_valik = int(input(f"ВValige joonis 1, 2 või 3: "))
                if p1_valik not in [1, 2, 3]:
                    print("Vale valik, proovige uuesti.")
                    continue
            except ValueError:
                print("Vale valik, proovige uuesti.")
                continue

            print(f"{player2}, olemasolevad valikud 1)kivi, 2)käärid, 3)paber")
            try:
                p2_valik = int(input(f"Valige joonis 1, 2 või 3: "))
                if p2_valik not in [1, 2, 3]:
                    print("Vale valik, proovige uuesti.")
                    continue
            except ValueError:
                print("Vale valik, proovige uuеsti.")
                continue

            if p1_valik == 1:
                p1_choice = "kivi"
            elif p1_valik == 2:
                p1_choice = "käärid"
            elif p1_valik == 3:
                p1_choice = "paber"

            if p2_valik == 1:
                p2_choice = "kivi"
            elif p2_valik == 2:
                p2_choice = "käärid"
            elif p2_valik == 3:
                p2_choice = "paber"

            print(f"{player1} - {p1_choice}, {player2} - {p2_choice}")

            if p1_choice == p2_choice:
                print("Tie")
            elif (p1_choice == "kivi" and p2_choice == "käärid") or (p1_choice == "käärid" and p2_choice == "paber") or (p1_choice == "paber" and p2_choice == "kivi"):
                print(f"Võit {player1}")
                player1_point += 1
            else:
                print(f"Võit {player2}")
                player2_point += 1

            print(f"Счет: {player1} - {player1_point}, {player2} - {player2_point}")

            # Выход из игры
            exit_game = input("Kas soovite mängu jätkata? (jah/ei): ").strip().lower()
            if exit_game != "jah":
                break
    else:
        print("Vale valik, proovige uuesti")
else:
    print("Mäng lõppenud")
