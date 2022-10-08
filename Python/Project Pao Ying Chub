import random
user_pao=''
random_pao=''
result=''
win=0
loss=0
tile=0
print("Welcome to PAO YING CHUB")
while True:
    user_pao = input("Enter your choice (hammer, scissors, paper or exit) : ")
    if user_pao == "exit":
        break
    if user_pao == "hammer" or user_pao == "scissors" or user_pao == "paper":
        random_pao = random.choice(["hammer","scissors","paper"])
        if user_pao == random_pao:
            result = "tile"
            tile = tile + 1
        elif user_pao == "hammer" and random_pao == "paper":
            result = "lost"
            lost = lost + 1
        elif user_pao == "scissors" and random_pao == "hammer":
            result = "lost"
            lost = lost + 1
        elif user_pao == "paper" and random_pao == "scissors":
            result = "loss"
            loss = loss + 1
        else :
            result = "win"
            win = win + 1
        print(f"Your Choice is {user_pao} and Computer is {random_pao}")
        print(f"Result : {result}")
        print(f"Win :{win}  Tile : {tile} Loss : {loss}")
    else:
        print("Invalid Typing Please Try again")
