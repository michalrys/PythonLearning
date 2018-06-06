# 2018-06-06
# Autor: Michał Ryś
# InfoShare: day 03/04. Homework 01

# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:

  #
 ###
#####
#-------------------------------------------------------------------------------
# my idea :-D : draw it into following coordinate system:
#        1 2 3 4 5 6 7 ...
#      + - - - - - - - -
#   1  | s s s B s s s
#   2  | s s B B B s s
#   3  | s B B B B B s
#   4  | B B B B B B B
#  ...
#
#  then,  pyramid should be splitted into Mario's pyramid + stairs down
#
#  (Mario's pyr.)  (stairs down)
#        1 2 3 4   5 6 7 ...
#      + - - - - | - - - -
#   1  | s s s B | s s s
#   2  | s s B B | B s s
#   3  | s B B B | B B s
#   4  | B B B B | B B B
#  ... |
#
# So, when we have pyramid with 4 levels, we could say that we have:
# - in row 1: (4 - 1) empty space + 1 brick LEFT + (1-1) brick RIGHT + (4 - 1) empty space
# - in row 2: (4 - 2) empty space + 2 brick LEFT + (2-1) brick RIGHT + (4 - 2) empty space
# - in row 3: (4 - 3) empty space + 3 brick LEFT + (3-1) brick RIGHT + (4 - 3) empty space
# - in row 4: (4 - 4) empty space + 4 brick LEFT + (4-1) brick RIGHT + (4 - 4) empty space
#
# So, there is pattern like that:
# for n levels:
# - in row i: (i-1)empty space + (i)brick LEFT + (i-1)brick RIGHT + (i-1)empty space
#

# list of constance
PYRAMID_BRICK_MARK = '#'
PYRAMID_EMPTY_SPACE_MARK = ' '

# input data from user
pyramid_high_user_input = input('Wysokość piramidy wynosi: ')

# postprocessing
pyramid_high = int(pyramid_high_user_input)

# additional options like:
# offset from left
pyramid_offset_from_left = 5

# offset from top
pyramid_offset_from_top = 3

# offset from bottom
pyramid_offset_from_bottom = 3

# print offset from top
print(PYRAMID_EMPTY_SPACE_MARK, sep='', end=pyramid_offset_from_top * '\n')

# pyramid print out
for pyramid_level_from_top in range(1, pyramid_high + 1):
    pyramid_spaces_from_left_margin = pyramid_high - pyramid_level_from_top
    pyramid_bricks_stairs_left = pyramid_high - pyramid_spaces_from_left_margin
    pyramid_bricks_stairs_right = pyramid_bricks_stairs_left - 1
    pyramid_spaces_to_right_margin = pyramid_spaces_from_left_margin

    # print offset from left
    print(pyramid_offset_from_left * PYRAMID_EMPTY_SPACE_MARK, sep='', end='')

    # print pyramid
    print(pyramid_spaces_from_left_margin * PYRAMID_EMPTY_SPACE_MARK, sep='', end='')
    print(pyramid_bricks_stairs_left * PYRAMID_BRICK_MARK, sep='', end='')
    print(pyramid_bricks_stairs_right * PYRAMID_BRICK_MARK, sep='', end='')
    print(pyramid_spaces_to_right_margin * PYRAMID_EMPTY_SPACE_MARK, sep='', end='\n')

# print offset from bottom
print(PYRAMID_EMPTY_SPACE_MARK, sep='', end= pyramid_offset_from_bottom * '\n')

# TODO: base on that, Christmass tree could be build
# TODO: change it to function --> input args: offesets, size,
# TODO:                                         chars for brick and empty space.



