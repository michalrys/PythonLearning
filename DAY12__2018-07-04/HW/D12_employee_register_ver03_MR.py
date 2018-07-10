# 2018-07-10, M. Ryś
# EmployeeRegister - ver 3
# ------------------------------------------------------------------------------


class Work:
    def __init__(self):
        self.__name = ''
        self.__positions = {}

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @property
    def positions(self):
        return self.__positions

    def add_position(self, location_in_hierarchy, title):
        try:
            location = int(location_in_hierarchy)
        except ValueError:
            print('Location must be integer > 0. Aborted.')
            return
        else:
            if location > 0:
                self.__positions[location] = str(title)
                return
            else:
                print('Location must be integer > 0. Aborted.')
                return

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


class Worker:
    __salary_periods = {'h': 'per hour',
                        'd': 'per day',
                        'w': 'per week',
                        'm': 'per month',
                        'y': 'per year'}

    @classmethod
    def salary_periods_info(cls):
        print(f'\tAllowable salary periods are:')
        for period in Worker.__salary_periods.keys():
            print(f'\t\tUse symbol "{period}" '
                  f'for salary {Worker.__salary_periods[period]}')

    def __init__(self, name='Unknown',
                 lastname='Unknown',
                 salary='0.00',
                 salary_period='y'):
        self.__name = name
        self.__lastname = lastname
        self.__work = None
        self.__work_position = {}
        self.__login = ''

        try:
            salary = float(salary)
        except ValueError:
            print(f'\tValue "{salary}" is wrong input salary. '
                  f'It must be positive float number. Correct this '
                  f'later. Value of 0.00 was assumed for salary.')
            self.__salary = float(0)
        else:
            if salary < 0:
                print(f'\tValue "{salary}" is wrong input salary. '
                      f'It must be positive float number. Correct this '
                      f'later. Value of 0.00 was assumed for salary.')
                self.__salary = float(0)
            else:
                self.__salary = float(salary)

        if salary_period in Worker.__salary_periods.keys():
            self.__salary_period = salary_period
        else:
            print(f'\tError: Given "{salary_period}" is wrong salary period. '
                  f'Correct this later. Salary period "y" was assumed')
            self.__salary_period = 'y'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def full_name(self):
        return f'{self.lastname.capitalize()}, {self.name.capitalize()}'

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = str(value)

    @property
    def salary(self):
        return f'{float(self.__salary):.2f}'

    @salary.setter
    def salary(self, value):
        try:
            value = float(value)
        except ValueError:
            print(f'\tWrong value (it is not number) - salary was not updated.')
        else:
            if value < 0:
                print(f'Wrong value (must be possitive) '
                      f'- salary was not updated.')
            else:
                self.__salary = value

    @property
    def salary_period(self):
        return self.__salary_period

    @salary_period.setter
    def salary_period(self, value):
        if value in Worker.__salary_periods.keys():
            self.__salary_period = value
        else:
            print(f'Error: Given "{value}" is wrong salary period. '
                  f'It must be one of them:')
            for period in Worker.__salary_periods.keys():
                print(f'\tWrite "{period}" '
                      f'for salary {Worker.__salary_periods[period]}.')

    def add_salary(self, cash, per_time):
        self.salary = cash
        self.salary_period = per_time

    def period_change(self, new_period='y'):
        if new_period not in Worker.__salary_periods:
            print(f'\tWrong input. Write correct salary period.')
            return
        current_period = self.salary_period

        if current_period == new_period:
            pass
            # print(f'\tGiven salary period is current. Nothing was changed.')
        elif current_period == 'h':
            if new_period == 'd':
                self.salary_period = 'd'
                self.__salary = self.__salary * 8
            elif new_period == 'w':
                self.salary_period = 'w'
                self.__salary = self.__salary * 8 * 5
            elif new_period == 'm':
                self.salary_period = 'm'
                self.__salary = self.__salary * 8 * 5 * 4
            elif new_period == 'y':
                self.salary_period = 'y'
                self.__salary = self.__salary * 8 * 5 * 4 * 12
        elif current_period == 'd':
            if new_period == 'h':
                self.salary_period = 'h'
                self.__salary = self.__salary / 8
            elif new_period == 'w':
                self.salary_period = 'w'
                self.__salary = self.__salary * 5
            elif new_period == 'm':
                self.salary_period = 'm'
                self.__salary = self.__salary * 5 * 4
            elif new_period == 'y':
                self.salary_period = 'y'
                self.__salary = self.__salary * 5 * 4 * 12
        elif current_period == 'w':
            if new_period == 'h':
                self.salary_period = 'h'
                self.__salary = self.__salary / (8 * 5)
            elif new_period == 'd':
                self.salary_period = 'd'
                self.__salary = self.__salary / 8
            elif new_period == 'm':
                self.salary_period = 'm'
                self.__salary = self.__salary * 4
            elif new_period == 'y':
                self.salary_period = 'y'
                self.__salary = self.__salary * 4 * 12
        elif current_period == 'm':
            if new_period == 'h':
                self.salary_period = 'h'
                self.__salary = self.__salary / (8 * 5 * 4)
            elif new_period == 'd':
                self.salary_period = 'd'
                self.__salary = self.__salary / (5 * 4)
            elif new_period == 'w':
                self.salary_period = 'w'
                self.__salary = self.__salary / 4
            elif new_period == 'y':
                self.salary_period = 'y'
                self.__salary = self.__salary * 12
        elif current_period == 'y':
            if new_period == 'h':
                self.salary_period = 'h'
                self.__salary = self.__salary / (8 * 5 * 4 * 12)
            elif new_period == 'd':
                self.salary_period = 'd'
                self.__salary = self.__salary / (5 * 4 * 12)
            elif new_period == 'w':
                self.salary_period = 'w'
                self.__salary = self.__salary / (4 * 12)
            elif new_period == 'm':
                self.salary_period = 'm'
                self.__salary = self.__salary / 12

    @property
    def work(self):
        return self.__work

    @work.setter
    def work(self, value):
        if not isinstance(value, Work):
            print('\tWrong work. Work for employee was not updated.')
            return
        else:
            self.__work = value

    @property
    def position(self):
        return self.__work_position

    @position.setter
    def position(self, id_or_name):
        try:
            id_position = int(id_or_name)
        except ValueError:
            name_position = str(id_or_name)
            if name_position not in self.__work.positions.values():
                print('Wrong name of position. Must be one of them:')
                print(self.__work.positions)
                return
            else:
                for id_position in self.__work.positions.keys():
                    if name_position == self.__work.positions[id_position]:
                        self.__work_position = \
                            {id_position: self.__work.positions[id_position]}
                        return
        else:
            if not id_position > 0:
                print('Wrong id - must be > 0.')
                return
            else:
                if id_position in self.__work.positions.keys():
                    self.__work_position = \
                        {id_position: self.__work.positions[id_position]}
                    return
                else:
                    print('Wrong id - there is no such hierarchy for this work.'
                          ' Must be one of them:')
                    print(self.__work.positions)
                    return

    def __str__(self):
        return f'{self.name.capitalize()} {self.lastname[0:3].capitalize()}***'

    def __repr__(self):
        return self.__str__()


class Office:
    __salaries_global = float(0)
    #TODO: add method -> update __salaries_global

    @classmethod
    def __salaries_global_increase(cls, value):
        Office.__salaries_global += float(value)

    @classmethod
    def __salaries_global_decrease(cls, value):
        Office.__salaries_global -= float(value)

    def __init__(self, name='Unknown'):
        self.__name = name
        # keys = login, values = worker
        self.__workers = {}
        self.__salaries = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @property
    def workers(self):
        return self.__workers

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            print('Wrong input data - must be instance of worker.')
        else:
            self.__workers[worker.login] = worker
            worker.period_change('y')
            self.__salaries += float(worker.salary)

    def remove_worker(self, worker):
        if not isinstance(worker, Worker):
            print('Wrong input data - must be instance of worker.')
        else:
            del self.__workers[worker.login]
            worker.period_change('y')
            self.__salaries -= float(worker.salary)

    @property
    def salaries(self):
        return f'{self.__salaries:.2f}'

    @property
    def salaries_update(self):
        self.__salaries = 0
        for worker in self.__workers.values():
            self.__salaries += float(worker.salary)
        return f'\tOffice: "{self.name}" - salaries were updated.'

    def add_cleaners(self, cleaner_per_regular_workers=7):
        how_many_regular_workers = 0
        how_many_cleaners = 0
        how_many_cleaners_should_be = 0
        how_many_cleaners_to_add = 0
        for worker in self.__workers.values():
            if not worker.work == cleaner_work:
                how_many_regular_workers += 1
            if worker.work == cleaner_work:
                how_many_cleaners += 1

        print(f'\tIn office "{self.name}" are {how_many_regular_workers} '
              f'regular workers and {how_many_cleaners} cleaners.')

        if how_many_regular_workers < cleaner_per_regular_workers:
            how_many_cleaners_should_be = 1
        else:
            how_many_cleaners_should_be = \
                cleaner_per_regular_workers // how_many_regular_workers

        if how_many_cleaners_should_be > how_many_cleaners:
            how_many_cleaners_to_add = \
                how_many_cleaners_should_be - how_many_cleaners

        print(f'\tThere should be {how_many_cleaners_to_add} additional '
              f'cleaners in office.')

        if how_many_cleaners_to_add > 0:
            # add anonymous cleaners to office
            temp_cleaner_list = []

            for temp_id in range(how_many_cleaners_to_add):
                temp_name = 'Temporary cleaner ' + str(temp_id)
                temp_cleaner_list.append(Worker(temp_name, '', 1000, 'w'))
                temp_cleaner_list[temp_id].work = cleaner_work
                temp_cleaner_list[temp_id].position = 1
                temp_cleaner_list[temp_id].login = \
                    'cleaner_temp_' + str(temp_id)
                self.add_worker(temp_cleaner_list[temp_id])

            print(f'\tSevaral temporary cleaners were added to worker list. '
                  f'\n\tThey are temporary workers, only for test calculation. '
                  f'It is recommended to delete them, '
                  f'and add cleaners in standard way.')

    @property
    def salaries_per_year_summary(self):
        for worker in self.__workers.values():
            worker.period_change('y')
        self.salaries_update
        return f'{self.__salaries:.2f}'

    def __str__(self):
        return f'"{self.name}"'

    def __repr__(self):
        return self.__str__()


# create kind of works
cleaner_work = Work()
cleaner_work.name = 'Cleaner'
cleaner_work.add_position(1, 'Cleaner for everything')
cleaner_work.add_position(2, 'Cleaner of secret data')
print(cleaner_work, cleaner_work.positions)
driver_work = Work()
driver_work.name = 'Driver cat.B'
driver_work.add_position(1, 'Local driver')
driver_work.add_position(2, 'International driver')
driver_work.add_position(3, 'Special delivers driver')
driver_work.add_position(4, 'Boss driver')
print(driver_work, driver_work.positions)
engineer_work = Work()
engineer_work.name = 'Engineer'
engineer_work.add_position(1, 'Assistant')
engineer_work.add_position(2, 'Junior')
engineer_work.add_position(3, 'Regular')
engineer_work.add_position(4, 'Senior')
engineer_work.add_position(5, 'Master')
engineer_work.add_position(6, 'Expert')
print(engineer_work, engineer_work.positions)

# create workers
jkowalski = Worker('jan', 'kowalski', 1000, 'w')
jkowalski.work = driver_work
jkowalski.position = 1
jkowalski.login = 'jkowalski'
print(jkowalski.login, jkowalski.work, jkowalski.position)
print(jkowalski.full_name, jkowalski.salary, jkowalski.salary_period)

anowak = Worker()
anowak.salary = 2500
anowak.salary_period = 'd'
anowak.name = 'anna'
anowak.lastname = 'nowak'
anowak.login = 'anowak2'
# anowak.salary_periods_info()
print(anowak.full_name, anowak.salary, anowak.salary_period)

anowak.period_change('y')
print(anowak.full_name, anowak.salary, anowak.salary_period)

anowak.work = engineer_work
anowak.position = 3
print(anowak.login, anowak.work, anowak.position)


jkowalski2 = Worker('jan', 'kowalski', 1000, 'w')
jkowalski2.work = engineer_work
jkowalski2.position = 1
jkowalski2.login = 'jkowalski2'

jkowalski3 = Worker('jan', 'kowalski', 1000, 'w')
jkowalski3.work = engineer_work
jkowalski3.position = 1
jkowalski3.login = 'jkowalski3'

# jkowalski4 = Worker('jan', 'kowalska', 1000, 'w')
# jkowalski4.work = cleaner_work
# jkowalski4.position = 1
# jkowalski4.login = 'jkowalski4'

# create office
print(85*'*')
office_01 = Office()
office_01.name = 'Station no 1 - KRK'
office_01.add_worker(anowak)
office_01.add_worker(jkowalski)
office_01.add_worker(jkowalski2)
office_01.add_worker(jkowalski3)
# office_01.add_worker(jkowalski4)


print(office_01, office_01.workers, office_01.salaries)
print(jkowalski.salary, jkowalski.salary_period)
print(anowak.salary, anowak.salary_period)

anowak.salary = 5000
print(anowak.salary, anowak.salary_period)
print(office_01.salaries_update)
print(office_01, office_01.workers, office_01.salaries)

# add cleaners
office_01.add_cleaners()
print(office_01.workers)

# salary summary
print(office_01.salaries)
print(office_01.salaries_per_year_summary)
