# Default values for machine.
water = 400
milk = 540
beans = 120
cups = 9
money = 550

# Prints current machine inventory quantities
def print_inventory(water, milk, beans, cups, money):
    print("The coffee machine has:")
    print(str(water) + " ml of water")
    print(str(milk) + " ml of milk")
    print(str(beans) + " g of coffee beans")
    print(str(cups) + " disposable cups")
    print("$" + str(money) + " of money\n")

possible_cups = 0
add_water = 0
add_milk = 0
add_beans = 0
add_cups = 0

print("Write action (buy, fill, take, remaining, exit): ") 
choice = input()

while choice != "exit":
    if choice == "fill":
        print("Write how many ml of water you want to add:") 
        add_water = int(input())
        water += add_water
        print("Write how many ml of milk you want to add:")  
        add_milk = int(input())
        milk += add_milk
        print("Write how many grams of coffee beans you want to add:")  
        add_beans = int(input())
        beans += add_beans
        print("Write how many disposable cups you want to add:") 
        add_cups = int(input())
        cups += add_cups
        print("\n")
    
    elif choice == "take":
        print("I gave you $" + str(money) + "\n")
        money = 0
    
    elif choice == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        option = input()
        if option == "1":
            if water >= 250 and beans >= 16 and money >= 4 and cups > 0:
                water -= 250
                beans -= 16
                money += 4
                cups -= 1
                print("I have enough resources, making you a coffee!\n")
            else:
                if water < 250:
                    print("Sorry, not enough water!")
                elif beans < 16:
                    print("Sorry, not enough beans!")
                elif money < 4:
                    print("Sorry, not enough money!")
                else:
                    print("Sorry, not enough cups!")
        elif option == "2":
            if water >= 350 and milk >= 75 and beans >= 20 and money >= 7 and cups > 0:
                water -= 350
                milk -= 75
                beans -= 20
                money += 7
                cups-= 1
                print("I have enough resources, making you a coffee!\n")
            else:
                if water < 350:
                    print("Sorry, not enough water!")
                elif milk < 75:
                    print("Sorry, not enough milk!")
                elif beans < 20:
                    print("Sorry, not enough beans!")
                elif money < 7:
                    print("Sorry, not enough money!")
                else:
                    print("Sorry, not enough cups!")
        elif option == "3":
            if water >= 200 and milk >= 100 and beans >= 12 and money >= 6 and cups > 0:
                water -= 200
                milk -= 100
                beans -= 12
                money += 6
                cups -= 1
                print("I have enough resources, making you a coffee!\n")
            else:
                if water < 200:
                    print("Sorry, not enough water!")
                elif milk < 100:
                    print("Sorry, not enough milk!")
                elif beans < 12:
                    print("Sorry, not enough beans!")
                elif money < 6:
                    print("Sorry, not enough money!")
                else:
                    print("Sorry, not enough cups!")
        
        elif option == "back":
            print("Write action (buy, fill, take, remaining, exit): ")
            choice = input()
            continue
        
        else:
            continue
            
    elif choice == "remaining":
        print_inventory(water, milk, beans, cups, money)
        
    else:
        exit()
    
    print("Write action (buy, fill, take, remaining, exit): ")
    choice = input()
exit()
