# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework

# stworz macierz (4 x 5), ktorej wszystkie komorki wypelnione sa znakiem *
# ------------------------------------------------------------------------------

# functions
def get_matrix_with_special_char(special_char, rows, columns):
    #TODO make more complex
    single_row = int(columns) * [special_char]
    matrix = int(rows) * [single_row]
    return matrix

def print_matrix_2d(matrix):
    #TODO make more complex
    for row in matrix:
        print('|', sep=' ', end='')
        for element in row:
            print( ' ', element, ' ', sep='', end='')
        print('|', sep=' ', end='\n')

# main
matrix_4x5 = get_matrix_with_special_char('*', 4, 5)
print_matrix_2d(matrix_4x5)


