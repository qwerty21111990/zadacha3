class Tomato:
    states = {0: 'green', 1: 'yellow', 2: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 2:
            self._state += 1
        else:
            self._state += 0

    def is_ripe(self):
        if self._state == 2:
            return True
        return False


class TomatoBush:

    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(amount)]

    def grow_all(self):
        for item in self.tomatoes:
            item.grow()

    def all_are_ripe(self):
        return all(item.is_ripe() for item in self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает')
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Собрали весь урожай')
        else:
            print('Не все созрело')

    @staticmethod
    def knowledge_base():
        print('Здесь должна быть справка по садоводству')


Gardener.knowledge_base()
bush = TomatoBush(6)
gardener = Gardener('Ivan', bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
