# jak wyswietlic aktualna godzine i dzien

from time import gmtime, strftime
czas = strftime("%Y-%m-%d--%H-%M-%S", gmtime())

print(czas)

print(type(czas))