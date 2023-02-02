# Mothy Hall problem

import random

doors = [0,0,0]
winning_door = random.randint(0,2)
my_first_door_choice = random.randint(0,2)
doors[winning_door] = 1

wins_switch = 0
loses_switch = 0
wins_stay = 0
loses_stay = 0

for i in range (0,100000):
    while True:
        monthy_opens = random.randint(0,2)

        if (monthy_opens != winning_door) or (monthy_opens != my_first_door_choice):
            doors = monthy_opens
            break

    switch = [True,False]
    switch_door = random.choice(switch)
    while True:

        my_new_choice = random.randint(0,2)
        if switch_door == True:


            if (my_new_choice != monthy_opens) or (my_new_choice != my_first_door_choice):

                if my_new_choice == winning_door:
                    print("you win")
                    print(switch_door)
                    print()
                    wins_switch += 1
                    break
                else:
                    print("u loose")
                    print(switch_door)
                    print()
                    loses_switch += 1
                    break    

        else:
            if my_new_choice == winning_door:
                print("you win")
                print(switch_door)
                print()
                wins_stay += 1
                break
            else:
                print("u loose")
                print(switch_door)
                print()
                loses_stay += 1
                break    
    
print("wins stay: ",wins_stay)
print("loses stay: ",loses_stay)
print("wins switch: ",wins_switch)
print("loses switch: ",loses_switch)


    