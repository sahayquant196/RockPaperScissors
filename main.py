from game import Game
import utils
if __name__ == "__main__":
    player1_name,userinput = utils.user_inputs()
    Game = Game(player1_name,userinput)
    Game.startGame()
