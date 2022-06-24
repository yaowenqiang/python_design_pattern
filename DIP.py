# DIP Dependency inversion principle
from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Persion:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser): # low-level
    def __init__(self):
        self.relations = []


    def add_parent_ahd_child(self, parent, child):
        self.relations.append(
            ( parent, Relationship.PARENT, child)
        )

        self.relations.append(
            ( child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research: # High level module
    #def __init__(self, relationships):
    #    relations = relationships.relations
#
#        for r in relations:
#            if r[0].name =='John' and r[1] == Relationship.PARENT:
                #print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}.')


parent = Persion('John')
child1 = Persion('Chris')
child2 = Persion('Matt')

relationships = Relationships()

relationships.add_parent_ahd_child(parent, child1)
relationships.add_parent_ahd_child(parent, child2)


Research(relationships)
