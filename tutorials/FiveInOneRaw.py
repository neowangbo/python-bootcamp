class FiveInOneRaw:

    board = [' '] * 10;
    
    success = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(2,5,7))
    
    def judgeSuccess(self,player,steps):
        if steps >= 5:
            for elements in self.success:
                count = 0
                raw = [self.board[x] for x in elements]
                # print(raw)
                if raw == [player] * 3:
                    return True
        return False    
            
    
    def displayBoard(self):
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")
        print('---|---|---')
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print('---|---|---')
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")


    def run(self):
        print('Welcome play Five-In-One-RAW game!\n2 players rotate to input the number 1~9 which presents the location where you want to play.\n[s] - Start game; [r] - Restart game; [q]-Quite game.')

        while True:
            action = input('> ').lower()
            if action == '':
                continue
            elif action == 's':
                # start playing
                print('Loading game ......')
                self.start()
            elif action == 'r':
                continue
            elif action == 'q':
                break
            else:
                print('Please input valid character, [s] - Start game; [r] - Restart game; [q]-Quite game.')
                continue


    def start(self):
        round = 0
        while True:
            placeStr = ''
            player = ' '
            place = 0
            try:
                if round % 2 == 0:
                    placeStr = input("Now is O's turn: ").lower()
                    player = 'O'
                else:
                    placeStr = input("Now is X's turn: ").lower()
                    player = 'X'

                place = int(placeStr)

                if place <= 0 or place > 9:
                    raise FiveInOneRawNumberException()

                if self.board[place] != ' ':
                    raise FiveInOneRawPlaceException()

            except FiveInOneRawNumberException:
                print('Please input one 1~9 number.')
                continue
            except FiveInOneRawPlaceException:
                print('The location you input already has value, please reinput.')
                continue
            except:
                if placeStr == 'q':
                    break
                else:
                    print('Please input one 1~9 number.')
                    continue
                    
            round += 1
            self.board[place] = player
            self.displayBoard()
            if self.judgeSuccess(player,round):
                print(f'{player} win the game!')
                break;

    def restart(self):
        pass


class FiveInOneRawNumberException(Exception):
    pass

class FiveInOneRawPlaceException(Exception):
    pass    

if __name__ == '__main__':
    game = FiveInOneRaw()
    game.run()