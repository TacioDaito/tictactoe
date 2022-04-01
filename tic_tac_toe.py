from IPython.display import clear_output
import random
import time


class player:
    '''
    Improves the readability of player data and its manipulation. Attributes: 
    id (int), initials and mark (both str).
    '''

    def __init__(self, id, initials='', mark=''):
        self.id = id
        self.initials = initials
        self.mark = mark


def tic_tac_toe():
    '''
    Main function that runs the whole game. Has no arguments; returns None.
    '''
    def input_handler(an_input, input_type):
        '''
        Classifies inputs throughout the main function. Arguments: an_input and 
        input_type (both str); returns a str flag about the input.
        '''
        if an_input.upper() == 'Q':
            clear_output()
            print('Game Over.')
            return 'quit'
        elif an_input.upper() == 'B':
            return 'back'
        if input_type == 'initials':
            if an_input.isalpha() and len(an_input) == 3:
                return 'initials'
            else:
                print(f'\nPlease enter only 3 letters!')
                time.sleep(3)
                return 'invalid'
        elif input_type == 'moves':
            if an_input.isdecimal():
                if 0 < int(an_input) < 10:
                    return 'moves'
                else:
                    print(f'\nPlease enter an interger between 1 and 9!')
                    time.sleep(3)
                    return 'invalid'

    game_state = 'start'

    while game_state == 'start':
        '''
        In this function, while loops define game states. The start game
        state is the first one of them, where the game is announced.
        '''
        clear_output()
        print('\nx|o|x|o|x|o|x|o|x|o|x|o|x|o|x|o|x|')
        print('--[ TIC TAC TOE ]-------------------')
        print('o|x|o|x|o|x|o|x|o|x|o|x|o|x|o|x|o|')
        print('\nFight for the space in the board')
        print('and complete a full row to win! ')
        print('\nThis game is for 2 players.')
        print('\nEnter [B] to return to the')
        print('previous menu.')
        print('\nEnter [Q] to exit the game at')
        print('any time.')

        current_input = input('Press Enter to Start!')
        input_result = input_handler(current_input, None)
        if input_result == 'quit':
            return
        game_state = 'naming_p1'

        while game_state == 'naming_p1':
            '''
            Game state where players choose their 3-letter initials and 
            whether they want to be player 1 or 2.
            '''
            clear_output()
            player_1, player_2 = (player(id=1), player(id=2))
            current_input = input(
                'Enter your initials, Player 1 (3 letters): ').upper()
            input_result = input_handler(current_input, 'initials')
            if input_result == 'initials':
                player_1.initials = current_input
                pass
            elif input_result == 'invalid':
                continue
            elif input_result == 'back':
                game_state = 'start'
                break
            elif input_result == 'quit':
                return
            game_state = 'naming_p2'

            while game_state == 'naming_p2':
                '''
                Player 2's turn to choose their initials.
                '''
                clear_output()
                current_input = input(
                    'Player 2 enter your initials (3 letters): ').upper()
                input_result = input_handler(current_input, 'initials')
                if input_result == 'initials':
                    player_2.initials = current_input
                    pass
                elif input_result == 'invalid':
                    continue
                elif input_result == 'back':
                    game_state = 'naming_p1'
                    break
                elif input_result == 'quit':
                    return
                game_state = 'coin_toss'

                while game_state == 'coin_toss':
                    '''
                    In this game state a random binary event decides which
                    player will use the X mark and open the match.
                    '''
                    clear_output()
                    player_1.mark, player_2.mark = (
                        'X', 'O') if random.getrandbits(1) == 0 else ('O', 'X')
                    players = [player_1, player_2]
                    players.sort(key=lambda x: x.mark, reverse=True)
                    print(
                        f'(P{players[0].id}){players[0].initials} got lucky ' +
                        'and will open the match!')
                    time.sleep(2)
                    space_list = [' ']*9
                    game_state = 'match'

                    while game_state == 'match':
                        '''
                        The main game state, where the game is actually played. 
                        On every turn: The board is redrawed; win, loss and 
                        draw are checked; player's input are interpreted and
                        executed; player's switch turns.
                        '''
                        clear_output()
                        print(
                            f'\n {space_list[6]} | {space_list[7]} | ' +
                            f'{space_list[8]} ')
                        print(
                            f' {space_list[3]} | {space_list[4]} | ' +
                            f'{space_list[5]} ')
                        print(
                            f' {space_list[0]} | {space_list[1]} | ' +
                            f'{space_list[2]} ')

                        time.sleep(0.5)

                        if ['X', 'X', 'X'] in [(space_list[6:]),
                                               (space_list[3:6]
                                                ), (space_list[0:3]),
                                               (space_list[0:7:3]
                                                ), (space_list[1:8:3]),
                                               (space_list[2::3]
                                                ), (space_list[0::4]),
                                               (space_list[2:7:2])]:
                            winner = (players[0] if players[0].mark == 'X' else 
                            players[1])
                            print(
                                f'\n(P{winner.id}){winner.initials} WIN!')
                            time.sleep(3)
                            game_state = 'coin_toss'
                            break
                        elif ['O', 'O', 'O'] in [(space_list[6:]),
                                                 (space_list[3:6]
                                                  ), (space_list[0:3]),
                                                 (space_list[0:7:3]
                                                  ), (space_list[1:8:3]),
                                                 (space_list[2::3]
                                                  ), (space_list[0::4]),
                                                 (space_list[2:7:2])]:
                            winner = (players[0] if players[0].mark == 'O' else 
                            players[1])
                            print(
                                f'\n(P{winner.id}){winner.initials} WIN!')
                            time.sleep(3)
                            game_state = 'coin_toss'
                            break
                        elif ' ' not in space_list:
                            print('\nDRAW!')
                            time.sleep(3)
                            game_state = 'coin_toss'
                            break

                        print(
                            f'\nTurn: {players[0].mark} (P{players[0].id})'+
                            f'{players[0].initials}')

                        time.sleep(0.5)

                        current_input = input(
                            'Select a space to mark (1~9): ').upper()
                        input_result = input_handler(current_input, 'moves')
                        if input_result == 'moves':
                            input_space = current_input
                            pass
                        elif input_result == 'invalid':
                            continue
                        elif input_result == 'back':
                            game_state = 'naming_p2'
                            break
                        elif input_result == 'quit':
                            return
                        input_space = int(input_space) - 1
                        if space_list[input_space] not in ['X', 'O']:
                            space_list[input_space] = players[0].mark
                        else:
                            print('\nThis space is already occupied!')
                            time.sleep(3)
                            continue

                        players.reverse()
