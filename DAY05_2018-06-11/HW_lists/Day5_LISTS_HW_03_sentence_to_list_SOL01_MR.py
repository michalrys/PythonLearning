# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework 03

# program ktory zmieni zdanie w liste wyrazow
# zdanie = "Ala ma kota, kot ma Ale"
# ------------------------------------------------------------------------------

# constants
MESSAGE_SENTENCE_REVIEW = 'Twoje zdanie to: {sentence}.'
MESSAGE_SENTENCE_TYPE = 'Typ zmiennej to: {sentence_type}'
MESSAGE_SPLIT = '--------------------------------------------------------------'

# input sentence
sentence_input = 'Ala ma kota, kot ma Ale'
sentence_input_type = type(sentence_input)

# change to list
sentence_list = sentence_input.split(' ')
sentence_list_type = type(sentence_list)

# print out
print(MESSAGE_SENTENCE_REVIEW.format(sentence=sentence_input))
print(MESSAGE_SENTENCE_TYPE.format(sentence_type=sentence_input_type))
print(MESSAGE_SPLIT)
print(MESSAGE_SENTENCE_REVIEW.format(sentence=sentence_list))
print(MESSAGE_SENTENCE_TYPE.format(sentence_type=sentence_list_type))