import random
from connector import update_game


class LuckyGame:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.myChangeBox = 2
        self.myScore = 0
        self.total_boxes = 0
        self.mojeze = 0
        self.GoldCoin = 0
    
    def change(self):
        now_score = 0
        sample_list = ['Normal Box', 'Rare Box', 'Epic Box', 'Legendary Box', 'chance again', 'point 200']
        randomit = random.choices(sample_list, weights=(600, 350, 150, 30, 140, 6))
        print(f'Box: {randomit}')
        
        if randomit == ['Normal Box']:
            self.myScore += 15
            now_score = 15
            self.GoldCoin += 2
        elif randomit == ['Rare Box']:
            self.myScore += 30
            now_score = 30
            self.GoldCoin += 4
        elif randomit == ['Epic Box']:
            self.myScore += 60
            now_score = 60
            self.GoldCoin += 8
        elif randomit == ['Legendary Box']:
            self.myScore += 120
            now_score = 120
            self.GoldCoin += 16
        elif randomit == ['chance again']:
            self.myChangeBox += 1
            now_score = 0
        elif randomit == ['point 200']:
            self.myScore += 200
            now_score = 200
            self.mojeze += 1
            self.GoldCoin += 50
            print(f'♥♥♥ mojeze: {self.mojeze}')

        self.myChangeBox -= 1
        self.total_boxes += 1
        print("Chane Box:", self.myChangeBox)
        print("Your Total Scores:", self.myScore)
        print("Your score from  this box:", now_score)

    def lucky_game(self):
        while True:
            luckyGame = input("Open the box width: 'openbox' OR finish with: 'exit'>>>")
            if luckyGame == 'openbox':
                if self.myChangeBox != 0:
                    self.change()
                        
                else:
                    print()
                    print("NO...\tRemaining chance: 0")
                    
            elif luckyGame == "exit":
                self.starter()

            if self.myChangeBox == 0 and self.myScore < 30:
                print()
                print("you not lucky enough! try again...")
                print("total boxes:", self.total_boxes)
                print(100*'-')
                self.status2()
                exit()
            else:
                self.lucky_game()
           
    def starter(self):
        while True:
            starter = input("lucky game, store, status, for end program \"exit\">>>")
            if starter == "lucky game":
                self.lucky_game()
            elif starter == "stats":
                self.status()
            elif starter == "store":
                self.store()
            elif starter == "exit":
                print(100*'-')
                self.status2()
                update_game()
                exit()
            else:
                print("lucky game, store, for end program \"exit\">>>")

    def store(self):
        while True:
            print("your Score:", self.myScore, "your chances:", self.myChangeBox)
            store = input("30 Scores for 1 chance: \"buy\" exit: \"exit\">>>")
            if store == "buy":
                if self.myScore < 30:
                    print("not enough Score")
                    if self.myChangeBox > 0:
                        self.lucky_game()
                    else:
                        self.status2()
                        exit()

                else:
                    self.myChangeBox += 1
                    self.myScore -= 30
                    print("purchase successful!")
            elif store == "exit":
                break

        self.lucky_game()
    
    def status(self):
        print(f'$$ GoldCoin: {self.GoldCoin}\nsum Score: {self.myScore}\t\tyour chances: {self.myChangeBox}'
              f'\ntotal box: {self.total_boxes}\t\tmojeze: {self.mojeze}')
        print()
        self.starter()

    def status2(self):
        print(f'$$ GoldCoin: {self.GoldCoin}\nsum Score: {self.myScore}\t\tyour chances: {self.myChangeBox}'
              f'\ntotal box: {self.total_boxes}\t\tmojeze: {self.mojeze}')
        print()

    
def update_sample_class():
    pass

