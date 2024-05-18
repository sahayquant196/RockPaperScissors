from Player import Player
import random
import pwinput
class Game:
    def __init__(self,player1_name,user_input):
        self.Player1 =Player(player1_name)
        self.Player2 = Player.ChoosePlayer(user_input)
        self.choices = ['Rock','Paper','Scissors']
        welcome = '''
            **************************************************
            **************************************************
            WELCOME TO THE WORLD OF ROCK, PAPER, SCISSORS
            **************************************************
            **************************************************
            '''
        print(welcome)
    def checkResult(self):
        player1_result = self.Player1.choice
        player2_result = self.Player2.choice
        if (player1_result == player2_result):
            print('It is a draw!')
        elif (player1_result == 'Rock'):
            if (player2_result == 'Paper'):
                print(self.Player2.Name + ' wins!')
            else:
                print(self.Player1.Name + ' wins!')
        elif (player1_result == 'Paper'):
            if (player2_result =='Scissors'):
                print(self.Player2.Name + ' wins!')
            else:
                print(self.Player1.Name + ' wins!')
        elif (player1_result == 'Scissors'):
            if (player2_result == 'Rock'):
                print(self.Player2.Name + ' wins!')
            else:
                print(self.Player1.Name + ' wins!')
        exit()

    def startGame(self):
        print('You have to choose 0 for rock, 1 for paper, 2 for scissors')
        if self.Player2.Name =='Computer':
            rand_select = random.randint(0,2)
            self.Player2.choice = self.choices[rand_select]
            prompt_string = self.Player1.Name + ' : please select your choice'
            player1_choice = input(prompt_string)
            print("\n" * 100)
            self.Player1.choice = self.choices[int(player1_choice)]

        else:
            prompt_string_1 = self.Player1.Name + ' : please select your choice'
            player1_choice = input(prompt_string_1)
            print("\n" * 100)
            prompt_string_2 = self.Player2.Name + ' : please select your choice'
            player2_choice = input(prompt_string_2)
            print("\n" * 100)
            self.Player1.choice = self.choices[int(player1_choice)]

            self.Player2.choice = self.choices[int(player2_choice)]
        self.checkResult()












