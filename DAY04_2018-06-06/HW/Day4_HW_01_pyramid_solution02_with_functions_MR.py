# 2018-06-08
# Autor: Michał Ryś
# InfoShare: day 03/04. Homework 01
# SOLUTION 2: use of functions

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
# functions:  ------------------------------------------------------------------
def draw_pyramid(brick, space, height, offset_left, offset_top, offset_bottom):
    # print offset from top
    if offset_top > 0:
        print(space, sep='', end=offset_top * '\n')

    # pyramid print out
    for pyramid_level_from_top in range(1, height + 1):
        pyramid_spaces_from_left_margin = height - pyramid_level_from_top
        pyramid_bricks_stairs_left = height - pyramid_spaces_from_left_margin
        pyramid_bricks_stairs_right = pyramid_bricks_stairs_left - 1
        pyramid_spaces_to_right_margin = pyramid_spaces_from_left_margin

        # print offset from left
        print(offset_left * space, sep='', end='')

        # print pyramid
        print(pyramid_spaces_from_left_margin * space, sep='', end='')
        print(pyramid_bricks_stairs_left * brick, sep='', end='')
        print(pyramid_bricks_stairs_right * brick, sep='', end='')
        print(pyramid_spaces_to_right_margin * space, sep='', end='')
        if pyramid_level_from_top < height + 1:
            print('\n', sep='', end='')

    # print offset from bottom
    if offset_bottom > 0:
        print(space, sep='', end=offset_bottom * '\n')

    return None

# MAIN PROGRAM -----------------------------------------------------------------
# list of constants

# # input data from user #TODO: check correctness of input data
# brick_in = input('Podaj symbol bloku piramidy: ')
# space_in = input('Podaj symbol pustej przestrzeni: ')
# pyramid_amount = int(input('Ile piramid narysowac: '))
#
# # definition of lists
# height = []
# left = []
# top = []
# bottom = []
#
# # input data from user: specification of pyramids
# for pyramid_id in range(pyramid_amount):
#     height.append(int(input(f'Piramida {pyramid_id}: wysokość = ')))
#     left.append(int(input(f'Piramida {pyramid_id}: offset od lewej = ')))
#     top.append(int(input(f'Piramida {pyramid_id}: offset od góry = ')))
#     bottom.append(int(input(f'Piramida {pyramid_id}: offset od dołu = ')))
#
# # print out pyramids
# for id in range(pyramid_amount):
#     draw_pyramid(brick_in, space_in, height[id], left[id], top[id], bottom[id])

# TODO: write function --> draw pyramids
# TODO: write function --> draw trees (leaf, levels, level_height, position)

# tree
brick = 'M'
draw_pyramid(brick, ' ', 3, 4+3, 0, 0)
draw_pyramid(brick, ' ', 5, 2+3, 0, 0)
draw_pyramid(brick, ' ', 7, 0+3, 0, 0)



