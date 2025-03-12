import random
mylist = ["kivi", "paber", "käärid"]


#Игра между человеком и роботом
player=input("Sisesta oma nimi: ")
player_point=0
robot_player=0
while True:
     print("Доступные выборы: 1)камень, 2)ножницы, 3)бумага")
     pvalik=int(input(f"Выберите фигуру 1, 2 или 3: "))
     robot_list=random.choice(mylist)
     if pvalik==1:
         p=("kivi")
     elif pvalik==2:
         p=("käärid")
     elif pvalik==3:
         p=("paber")
     else:
         print("Vale")
     print(f"{player} - {p}, robot - {robot_list}")
     if p==robot_list:  
        print("Ничья")
     elif p==1 and robot_list==2:
        print("Победа игрока")
     elif p==2 and robot_list==3:
        print("Победа игрока")
     elif p==3 and robot_list==1:
        print("Победа игрока")
     elif p==1 and robot_list==3:
        print("Победа робота")
     elif p==2 and robot_list==1:
        print("Победа робота")
     elif p==3 and robot_list==2:
        print("Победа робота")
     # elif (p==kivi and robot_list==käärid) or (p==käärid and robot_list==paber) or (p==paber and robot_list==kivi):  
     #    print("Победа игрока")
     # elif (p==kivi and robot_list==paber) or (p==käärid and robot_list==kivi) or (p==paber and robot_list==käärid):  
     #    print("Победа робота")




# robot_list=random.choice(mylist)
# print(robot_list)
robot_list=random.choice(mylist)
     