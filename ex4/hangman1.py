# hadar_t787, Hadar Treidel, 20325554

import hangman_helper


# constants
CHAR_A = 97
START_COUNT = 0
GAME_OVER = 6
LETTER = 1
MODE = 0
NUMBER_OF_LETTERS = 26

def concat_list(str_lst):
    """performs concatenation on list of strings and
       returns single string"""
    concatenation = str()
    for i in str_lst:
        concatenation += i
    return concatenation


def update_word_pattern(word, pattern, letter):
    """checks if letter is in word and if it is replaces same
       index space in pattern with letter"""
    word_to_list = list(word)
    pattern_to_list = list(pattern)
    counter = START_COUNT
    for i in word:
       if i == letter:
          pattern_to_list[counter] = letter
       counter += 1
    adjusted_pattern = concat_list(pattern_to_list)
    return adjusted_pattern


def filter_words_list(words, pattern, wrong_guess_lst):
    """recieves a list of words, a word pattern and a list, input
       must be either lowercase alphabet characters or "_" in all
       objects, will return a list with all possible words from first
       list that can possibly fit pattern"""
    length_filter = set()
    wrong_guess_filter = set()
    final_filter = set()
    for i in words:
        if len(i) == len(pattern):
            length_filter.add(i)
    for i in length_filter:
        counter = START_COUNT
        for j in i:
            if j not in wrong_guess_lst:
                counter += 1
        if counter == len(i):
            wrong_guess_filter.add(i)
    for i in wrong_guess_filter:
        counter = START_COUNT
        for j in range(len(i)):
            if i[j] == pattern[j] or pattern[j] == "_":
                counter += 1
        if counter == len(i):
            final_filter.add(i)
    return final_filter


def histogram(n, num_list):
    """recieves a positive integer and a list of numbers in
       range of 0 to n-1, returns relevant histogram"""
    L = []
    L_counter = START_COUNT
    histogram = []
    histogram_counter = START_COUNT
    for i in range(n):
        L.append(L_counter)
        L_counter += 1
    for i in L:
        histogram_counter = START_COUNT
        for j in num_list:
            if i == j:
                histogram_counter += 1
        histogram.append(histogram_counter)
    return histogram


def letter_to_index(letter):
 """
 Return the index of the given letter in an alphabet list.
 """
 return ord(letter.lower()) - CHAR_A


def index_to_letter(index):
 """
 Return the letter corresponding to the given index.
 """
 return chr(index + CHAR_A)


def choose_letter(words, pattern):
    """recieves a list of words and word pattern, all characters
       must be either lowercase english alphabet or "_", and
       returns most common letter (if there are two or more letters
       that are most common will return the first in the list)"""
    num_list = []
    for i in words:
        for j in i:
            num_list.append(letter_to_index(j))
    abc_histogram = histogram(NUMBER_OF_LETTERS, num_list)
    most_common_index = abc_histogram.index(max(abc_histogram))
    most_common_letter = index_to_letter(most_common_index)
    while most_common_letter in pattern:
        abc_histogram[most_common_index] = 0
        most_common_index = abc_histogram.index(max(abc_histogram))
        most_common_letter = index_to_letter(most_common_index)
    return most_common_letter


def give_hint(words_list, pattern, wrong_guess_list):
    """returns a hint in form of letter to user"""
    filtered_list = filter_words_list(words_list,
                            pattern, wrong_guess_list)
    hint_letter = choose_letter(filtered_list, pattern)
    msg = hangman_helper.HINT_MSG + hint_letter
    return msg


def winner_winner_chicken_dinner(word, pattern):
    """ recieves word, and pattern and checks if they are the same,
        if yes, return win message, if not, loss message """
    if pattern == random_word:
        msg = hangman_helper.WIN_MSG
    else:
        msg = hangman_helper.LOSS_MSG + random_word
    return msg
    


def run_single_game(words_list):
    """recieves list of words, chooses randomly one of them, and runs a single
       game of hangman, words must contain english alphabet only and only
       lowercase letters"""
    random_word = hangman_helper.get_random_word(words_list)
    pattern_starter = ['_'] * len(random_word)
    pattern = concat_list(pattern_starter)
    wrong_guess_list = []
    msg = hangman_helper.DEFAULT_MSG
    while len(wrong_guess_list) < GAME_OVER and pattern != random_word:
        hangman_helper.display_state(pattern, len(wrong_guess_list),
                                     wrong_guess_list, msg, ask_play=False)
        user_input = hangman_helper.get_input()
        guess = user_input[LETTER]
        if user_input[MODE] == hangman_helper.HINT:
            msg = give_hint(words_list, pattern, wrong_guess_list)
            hangman_helper.display_state(pattern, len(wrong_guess_list),
                                 wrong_guess_list, msg, ask_play=False)
        elif type(guess) == str:
            if len(guess) != 1 or str.isalpha(
                   guess) == False or str.islower(guess) == False:
                msg = hangman_helper.NON_VALID_MSG
            elif guess in wrong_guess_list or guess in pattern:
                msg = hangman_helper.ALREADY_CHOSEN_MSG + guess
            elif guess in random_word:
                pattern = update_word_pattern(random_word, pattern, guess)
                msg = hangman_helper.DEFAULT_MSG
            else:
                wrong_guess_list.append(guess)
                msg = hangman_helper.DEFAULT_MSG
    msg = winner_winner_chicken_dinner(random_word, pattern)
    hangman_helper.display_state(pattern, len(wrong_guess_list),
                                     wrong_guess_list, msg, ask_play=True)
        

def main():
    """runs full hangman game"""
    words_list = hangman_helper.load_words()
    run_single_game(words_list)
    new_game = hangman_helper.get_input()
    while new_game[1] == True:
        run_single_game(words_list)
        new_game = hangman_helper.get_input()

   
if __name__ == "__main__":
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()




    
        
        
    
