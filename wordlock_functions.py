""" Starter code for CSC108 Assignment 1 Winter 2020 """

# Game setting constants
SECTION_LENGTH = 3
ANSWER = 'CATDOGFOXEMU'

# Move constants
SWAP = 'S'
ROTATE = 'R'
CHECK = 'C'


def get_section_start(section_num: int) -> int:
    """ Return the starting index of the section corresponding to section_num.
    
    >>> get_section_start(1)
    0
    >>> get_section_start(3)
    6
    """
    return SECTION_LENGTH * (section_num - 1)


def is_valid_move(player_move: str) -> bool:
    """ Return whether or not player_move is valid.
    
    >>> is_valid_move('S')
    True
    >>> is_valid_move('R')
    True 
    """
    return player_move == SWAP or player_move == ROTATE or player_move == CHECK


def is_valid_section(sec_num: int) -> bool:
    """ Return whether sec_num is valid or not.

    >>> is_valid_section(1)
    True
    >>> is_valid_section(5)
    False
    """
    return (len(ANSWER) % sec_num) == 0 and ((SECTION_LENGTH * sec_num)
                                             <= len(ANSWER))


def check_section(game_state: str, valid_section_num: int) -> bool:
    """ Return whether game state game_state of section number
    valid_section_num matches that of the one in ANSWER.

    >>> check_section('CATDOGFOXEMU', 1)
    True

    >>> check_section('CATDOGFOXEMU', 2)
    True

    >>> check_section('CATDGOFOXEMU', 2)
    False
    """

    game_state_seq = game_state[(SECTION_LENGTH * (valid_section_num - 1)):
                                (SECTION_LENGTH * valid_section_num)]
    answer_seq = ANSWER[(SECTION_LENGTH * (valid_section_num - 1)):
                        (SECTION_LENGTH * valid_section_num)]
    return game_state_seq == answer_seq


def change_state(game_state: str, sec_num: int, player_move: str) -> str:
    """ Return updated game state game_state for the sequence number sec_num
    after entering move player_move.
    
    >>> change_state('TACDOGFOXEMU', 1, 'S')
    'CATDOGFOXEMU'
    >>> change_state('CATDOGOXFEMU', 3, 'R')
    'CATDOGFOXEMU'
    """

    # first = game_state[SECTION_LENGTH * (sec_num - 1)]
    # mid = game_state[(((SECTION_LENGTH * sec_num) - 1) - 1):
    #                  (SECTION_LENGTH * sec_num) - 1]
    # last = game_state[(SECTION_LENGTH * sec_num) - 1]
    # lfill = game_state[0:(SECTION_LENGTH * (sec_num - 1))]
    # rfill = game_state[(sec_num * SECTION_LENGTH):]
    # result_swap = rest_1 + last + mid + first + rest_2
    # result_rotate = rest_1 + last + first + mid + rest_2
    #
    # if player_move == SWAP:
    #     return result_swap
    # elif player_move == ROTATE:
    #     return result_rotate
    # else:
    #     return None
    if is_valid_section(sec_num):
        if player_move == ROTATE:
            return game_state[0:(SECTION_LENGTH * (sec_num - 1))] + \
                   game_state[(SECTION_LENGTH * sec_num) - 1] + \
                   game_state[SECTION_LENGTH * (sec_num - 1)] + \
                   game_state[(((SECTION_LENGTH * sec_num) - 1) - 1):
                              (SECTION_LENGTH * sec_num) - 1] + \
                   game_state[(sec_num * SECTION_LENGTH):]
            # lfill + last + first + mid + rfill
        elif player_move == SWAP:
            return game_state[0:(SECTION_LENGTH * (sec_num - 1))] + \
                   game_state[(SECTION_LENGTH * sec_num) - 1] + \
                   game_state[(((SECTION_LENGTH * sec_num) - 1) - 1):
                              (SECTION_LENGTH * sec_num) - 1] + \
                   game_state[SECTION_LENGTH * (sec_num - 1)] + \
                   game_state[(sec_num * SECTION_LENGTH):]
            # lfill + last + mid + first + rfill
        else:
            return None
    else:
        return None


def get_move_hint(game_state: str, sec_num: int) -> str:
    """ Return a hint in order to unscramble game_state game state for sequence
    number sec_num. 
    
    >>> get_move_hint('TACDOGFOXEMU', 1)
    'S' 
    >>> get_move_hint('CATODGFOXEMU', 2)
    'R'
    """
    game_state_seq = game_state[(3 * (sec_num - 1)):(3 * sec_num)]
    answer_seq = ANSWER[(3 * (sec_num - 1)):
                        (3 * sec_num)]
    if answer_seq != game_state_seq:
        if (game_state[1 + (3 * (sec_num - 1))] == ANSWER[1 +
                                                          (3 * (sec_num - 1))]):
            return SWAP
        elif game_state[((SECTION_LENGTH * (sec_num - 1)) + 1)] !=\
                ANSWER[((SECTION_LENGTH * (sec_num - 1)) + 1)]:
            return ROTATE
        else:
            return None
    else:
        return None
