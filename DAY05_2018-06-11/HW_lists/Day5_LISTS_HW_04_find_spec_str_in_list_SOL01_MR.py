# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework 03

# znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2
# ------------------------------------------------------------------------------

# constants
WORD_LENGTH_MINIMAL = 2
WORD_LETTER_ID_1 = 0
WORD_LETTER_ID_2 = -1

MESSAGE_INPUTS = 'List of words: {words}.'
MESSAGE_OUTPUTS = 'Amount of special words: {how_many}.'
MESSAGE_SEPARATION = 82 * '-'

# input data for tes
list_user = ['abc', 'xyz', 'aba', '1221']

# do
amount_of_special_words = 0

for word in list_user:
    word_length = len(word)
    if word_length >= WORD_LENGTH_MINIMAL:
        if word[WORD_LETTER_ID_1] == word[WORD_LETTER_ID_2]:
            amount_of_special_words += 1

# print out
print(MESSAGE_INPUTS.format(words=list_user))
print(MESSAGE_OUTPUTS.format(how_many=amount_of_special_words))

# ------------------------------------------------------------------------------
# method 2: functions
print(MESSAGE_SEPARATION)

def amount_of_special_words(list: list, word_length_min: int = 2,
                            letter_1_to_match: int = 0,
                            letter_2_to_match: int = -1) -> int:
    """Get amount of words from list of words which are:
    - length of word is more or equal /word_length_min/
    - word have two identical letters:
        - position of first letter in word is /letter_1_to_match/
        - position of second letter in word is /letter_2_to_match/

    :param list list: user input list of words.
    :param int word_length_min: minimal length of word
    :param int letter_1_to_match: first letter to match
    :param int letter_2_to_match: second letter to match
    :return int:  amount of words which fullfil requirements
    """
    amount_of_special_words = 0
    for word in list:
        word_length = len(word)
        if word_length >= word_length_min:
            if word[letter_1_to_match] == word[letter_2_to_match]:
                amount_of_special_words += 1

    return amount_of_special_words

how_many_words = amount_of_special_words(list_user)
# print out
print(MESSAGE_INPUTS.format(words=list_user))
print(MESSAGE_OUTPUTS.format(how_many=how_many_words))