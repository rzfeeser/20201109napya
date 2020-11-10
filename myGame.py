#!/usr/bin/env python3

class Player:
    def __init__(self, name, lifeno, controller):
        self.name = name
        self.lifeno = lifeno
        self.controller = controller
        self.score = 0
        self.world = 1

    def __str__(self):
        return self.name

    def changelives(self, lifech):
        self.lifeno = self.lifeno + lifech
        return self.lifeno

    def changescore(self, scorech):
        self.score = self.score + scorech
        return self.score

def main():
    # ready player 1!
    player1 = Player("Mario", 3, "port1")

    print(player1)

    print(dir(player1))

    print(player1.world)

    print(player1.score)


    # ready player2!
    player2 = Player("Luigi", "4", "port2")
    player3 = Player("Princess Toadstool", "3", "port3")


    print(player2.name)

    print(player3.controller)
    

    ## player1 just touched a GREEEN mushrooms! (+1 life)
    print("Congrats! Player1 just found a green mushroom!")
    print("Previous life total", player1.lifeno)
    print("New life total is", player1.changelives(1))


    print("Player2 just smashed a flying turtle!")
    print("Player2 score is", player2.changescore(100))
    print("Player2 just made it to the flagpole at the caslte!")
    print("Player2 score is", player2.changescore(10000))



main()
