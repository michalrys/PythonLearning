# 2018-06-07
# Author: Michał Ryś
# InfoShare: day 03/04. Homework 04

# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata
# ------------------------------------------------------------------------------

# constants legend:
#       DOG_AGE : age of user's dog
# _DESCRIPTION_ : characteristic point in dog life
#           _DY : biological age in years valid for human
#           _HY : biological age in years valid for dog
DOG_AGE_CRISIS_DY = 2.0
DOG_AGE_BEFORE_CRISIS_MULTI_HY = 10.5
DOG_AGE_AFTER_CRISIS_MULTI_HY = 4.0
DOG_AGE_LIMIT_DY = 40.0

# user input data
dog_age_in_human_years = float(input('Od ilu lat masz psa? >> '))

# check input data #TODO: float errors? split years & months

# age in dogs years

if dog_age_in_human_years > 0 and dog_age_in_human_years <= DOG_AGE_CRISIS_DY:
    # dog age before crisis
    dog_age_in_dog_years = \
        dog_age_in_human_years * DOG_AGE_BEFORE_CRISIS_MULTI_HY

elif dog_age_in_human_years > DOG_AGE_CRISIS_DY:
    # dog age after crisis = age part1 + age part2
    # dog age = age part1
    dog_age_in_dog_years = \
        DOG_AGE_CRISIS_DY * DOG_AGE_BEFORE_CRISIS_MULTI_HY

    # age part2: years after dog crisis
    dog_age_in_human_years_after_crisis = \
        dog_age_in_human_years - DOG_AGE_CRISIS_DY

    # dog age = sum (years before and after crisis)
    dog_age_in_dog_years += \
        dog_age_in_human_years_after_crisis * DOG_AGE_AFTER_CRISIS_MULTI_HY
else:
    print('Wrong input data.')

# print out
print(f'\nMasz psa od {dog_age_in_human_years:.1f} lat.')
print(f'Twój pies jest w wieku {dog_age_in_dog_years:.1f} lat.')

if dog_age_in_dog_years > DOG_AGE_LIMIT_DY:
    print(f'Zacznij szukać nowego psa :-(')

