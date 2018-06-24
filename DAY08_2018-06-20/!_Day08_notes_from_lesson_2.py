# 2018-06-18
# InfoShare: day 08.
# M. Ryś
#
# program do wprowadzania tylko liczb calkowitych

while True:
    number_user = input('Podaj wiek: ')
    try:
        number_user = int(number_user)
        # uwaga dla stringa 7.2 będzie błąd
        # aby to pomnąć, zamień str -> float -> int
        # czyli: int(float(number_user))
        break
    except ValueError:
        print('Błąd ! podaj liczbę całkowitą')

print('Twoj wiek to: ', number_user)

print(82 * '-')
# ------------------------------------------------------------------------------
# z iloscią prób
loop_current_iteration = 0
loop_end = 5
repeat_answer = True

while repeat_answer:
    number_user = input('Podaj wiek: ')
    try:
        number_user = int(number_user)
        break
    except ValueError:
        print('Błąd ! podaj liczbę całkowitą')
        loop_current_iteration += 1
        if loop_current_iteration == loop_end:
            print(f'Podales błędny wiek {loop_end} razy ! Przerywam tą zabawę.')
            break

print('Twoj wiek to: ', number_user)