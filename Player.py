class Player:
    def __init__(self,Name):
        self.__Name = Name
        self.Choice = None
    @property
    def Name(self):
        return self.__Name
    @classmethod
    def ChoosePlayer(cls,userinput):
        #
        if userinput == 'C':
            print('You are playing against computer')
            return cls('Computer')

        else:
            player_name = input('Enter name of Player2')
            print('You are playing against ' + player_name)
            return cls(player_name)
