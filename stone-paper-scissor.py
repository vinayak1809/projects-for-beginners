import random

loop = False


def game():
    pla_point = 0
    com_point = 0
    while not loop:
        li = ["stone", "paper", "scissor"]
        computer = random.choice(li)

        player = input("\nStone Paper or Scissor : ").lower()
        if player in li:
            print(f"\ncomputer's move : {computer}")

            if player == computer:
                print("tied")

            elif (player == "stone" and computer == "scissor") or (player == "paper" and computer == "stone") or (player == "scissor" and computer == "paper"):

                pla_point += 1
                print(
                    f"\nPoints : Player: {pla_point} and Computer: {com_point} ")

                if pla_point == 3:
                    print("Player won :) ")

            else:
                com_point += 1
                print(
                    f"Points : Computer: {com_point} and Player: {pla_point} ")

                if com_point == 3:
                    print("\ncomputer won :( ")

            if pla_point == 3 or com_point == 3:
                ask = input("\nenter to play again : ").lower()
                if ask:
                    game()

        else:
            print("guess \"stone, paper / scissor \"")


game()
