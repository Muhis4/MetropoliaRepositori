import random
class Player:
    def __init__(self, name, age):
        self.inventory = []
        self.name = name
        self.age = age
        self.gold = 0
    pass

class Mimi:
    def __init__(self):
        self.happiness = 80
        self.hunger = 80
        self.energy = 80
        self.entertainment = 80

    def ChangeHappiness(self):
        avarage = (self.energy + self.entertainment + self.hunger) / 3
        if(self.happiness < avarage):
            self.happiness += random.randint(6, 16)
        elif(self.happiness > avarage):
            self.happiness -= random.randint(6, 16)

        return self.happiness
    def Pet(self):

        randomFactor = random.uniform(0.2, 1.2)
        goldAmount = round(self.happiness * randomFactor)
        self.entertainment = min(100, self.entertainment + 4)
        self.energy = max(0, self.energy - 3)

        print(f"✨You've petted Mimi! She purrs and gives you {goldAmount} gold.")
        return goldAmount
    def Sleep(self):
        self.energy = min(100, self.energy + random.randint(80, 95))
        self.hunger = max(0, self.hunger - random.randint(20, 35))
        self.entertainment = max(0, self.entertainment - random.randint(15, 20))
        print("Mimi peacefully slept and now she feels well rested! But now she would like to have some food.")
        return self.energy
    def Eat(self, food = ""):
        if(food == ""):
            print("You gave her no food to eat and now she's concerned about your intellectual abilities...")
        elif food == "Basic cat food":
            self.hunger = min(100, self.hunger + 30)
        elif food == "Dalicacy fish":
            self.hunger = min(100, self.hunger + 60)
            self.happiness += 10
        return self.hunger
    def Play(self, toy = ""):
        if(toy == ""):
            print(f"You've played with Mimi! She enjoyed spending time with you. \n+ {15} entertainment. \n- 10 energy.")
            self.entertainment = min(100, self.entertainment + 15)
            self.energy = max(0, self.energy - 10)
        elif(toy =="Mouse toy"):
            print(f"You've played with Mimi! She enjoyed spending time with you. \n+ {40} entertainment. \n- 15 energy.")
            self.entertainment = min(100, self.entertainment + 40)
            self.energy = max(0, self.energy - 15)
        elif(toy =="Mouse toy"):
                print(f"You've played with Mimi! She enjoyed spending time with you. \n+ 70 entertainment. \n+ 20 happiness \n- 20 energy.")
                self.entertainment = min(100, self.entertainment + 70)
                self.energy = max(0, self.energy - 20)
                self.happiness += 20
        
        return self.entertainment
    def NextStep(self):
        self.energy -= 2
        self.hunger -= 4
        self.entertainment -= 3
        self.ChangeHappiness()
        if(self.happiness <= 0 or self.hunger <= 0 or self.entertainment <= 0 or self.energy <= 0):
            print("You're incapeble to take care of your cat! The police took Mimi from you for her own sake. \nYou lost.")
            exit()
class Item:
    def __init__(self, itemType, name, description, amount, statRegen, price):
        self.itemType = itemType
        self.name = name
        self.amount = amount
        self.statRegen = statRegen
        self.price = price
        self.description = description

class Shop:
    def __init__(self, player = Player("none", 0)):
        self.itemsList = self.CreateList()
        self.player = player
    def CreateList(self):
        description = "+30 hunger. \nA simple cat food containing sufficient nutrients and minerals to help your cat stay strong and healthy."
        basicFood = Item("Food","Basic cat food", description, 5, 30, 75)

        description = "+60 hunger. + 10 happiness.\nDelicious and nutritious Japanese fish! All cats love this kind of fish. It will leave your cat not only full but also happy!"
        delicacyFish = Item("BetterFood","Dalicacy fish", description, 2, 60, 200)

        description = "+40 entertainment. - 15 energy.\nA simple yet fun mouse. It can keep your cat occupied for a while."
        simpleToy = Item("Toy", "Mouse toy", description, 3, 40, 200)

        description = "+80 entertainment. +20 happiness. -20 energy.\nA premium, cool toy fish! It makes funny sounds and awakens your cat's hunting instincts."
        premiumToy = Item("BetterToy", "Premium fish toy", description, 2, 80, 400)

        return [basicFood, delicacyFish, simpleToy, premiumToy]
    def GiveList(self):
        print("Welcome to the shop! You can buy here whatever you want for your cat. To buy something just enter an item's name (won't happen if you don't have enough gold).\nTo leave enter leave.\nHere's list of our items:")
        for item in self.itemsList:
            print(f"Item: {item.name}, price: {item.price}.\n{item.description}")
            print("________________________________________________________________________")
        self.ShopLoop()
        
        return self.itemsList
    def ShopLoop(self):
        while True:
            com = input("Enter item: ")
            if(com == "leave"):
                print("You leave the shop and return to your home to your cat.")
                loop()
                break
            for item in self.itemsList:
                if com == item.name:
                    if(self.player.gold < item.price):
                        print("Not enough money.")
                    elif(self.player.gold >= item.price):
                        player.inventory.append(item.name)
                        player.gold -= item.price
            mimi.NextStep()
            
        return

def loop():
    while True:
        print(f"😸Mimi:\n😊Happiness: {mimi.happiness}.\n⚡Energy: {mimi.energy}.\n🍖Hunger: {mimi.hunger}.\n🎬Entertainment: {mimi.entertainment}.")
        print("___________________________")
        print(f"🎮Your inventory:")
        print(f"Gold: {player.gold}")
        print(player.inventory)
        print("\n1) Pet Mimi. 2) Feed Mimi. 3) Play with Mimi. 4) put to sleep. 5) go to the shop.")
        command= int(input("Please, enter number of command: "))
        if(command == 1):
            player.gold += mimi.Pet()
        elif(command == 2):
            food = input("Choose what to feed her from your inventory. Enter food's name (start with a capital letter): ")
            if food in player.inventory:
                player.inventory.remove(food)
                mimi.Eat(food)
            else:
                mimi.Eat()
        elif(command == 3):
            toy = input("Choose what to use to play with Mimi. (You can play with her without any toy): ")
            if toy in player.inventory:
                player.inventory.remove(toy)
                mimi.Play(toy)
            else:
                mimi.Play()
        elif(command == 4):
            mimi.Sleep()
        elif(command == 5):
            mimi.NextStep()
            shop.GiveList()
            mimi.NextStep()
            break
        mimi.NextStep()

        
print("Welcome to the Game!\nPlease, enter your name and age.")
player = Player(input("Name: "), int(input("Age: ")))
mimi = Mimi()
shop = Shop(player)
if(player.age < 12):
    print(f"Sorry {player.name}, you are not allowed to play this game.")
    exit()
with open("save.txt", "w") as save:
    save.write(f"Player's name: {player.name}. Age: {player.age}")
with open("intro.txt", "r") as intro:
    print(intro.read())
with open("instructions.txt", "r") as instructions:
    print(f"\n{instructions.read()}")

if(input("Press enter...") == ""):
    loop()