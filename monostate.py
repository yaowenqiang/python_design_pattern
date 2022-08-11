import random
import unittest
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        with  open('capitals.txt', 'r') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = \
                    int(lines[i+1].strip())


class ConfigurableRecordFinder:
    def __init__(self, db=Database()):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


class DummyDatabase:
    population = {
        'alpha':1,
        'beta':2,
        'gama':3,
    }

    def get_population(self, name):
        return self.population[name]

class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result

class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ["Beijing",'Shanghai']
        tp = rf.total_population(names)
        self.assertEqual(10000000 + 20000000, tp)


    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(6, crf.total_population(['alpha', 'beta', 'gama']))

if __name__ == '__main__':
    unittest.main()



