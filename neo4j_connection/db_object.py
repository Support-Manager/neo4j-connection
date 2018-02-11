
class DatabaseObject:
    def __init__(self, label, properties: list, related_from: list, related_to: list):
        self._label = label
        self._properties = properties
        self._related_from = related_from
        self._related_to = related_to


"""
from .errors import *
from . import __file__
import py2neo
import json

with open(__file__ + "/../config.json", 'r', encoding='utf-8') as f:
    config = json.load(f)


class DatabaseObject:
    _graph = py2neo.Graph(**config)
    _Node = py2neo.Node
    _Relationship = py2neo.Relationship

    def __init__(self, label: str, property_names: list, connected=False, autoincrement_property=None):

        self._label = label
        self._connected = connected
        self._property_names = property_names
        self._autoincrement = autoincrement_property

    def create(self):
        if self._connected:
            raise ObjectCreationError("Already connected to an existing object.")

        if self._autoincrement is not None:
            count = DatabaseObject._graph.run(f"MATCH (n:{self.label}) RETURN count(n)").evaluate()
            setattr(self, self._autoincrement, count + 1)

        tx = DatabaseObject._graph.begin()

        tx.create(DatabaseObject._Node(self.label, **self.properties))

        tx.commit()

        self._connected = True

    @property
    def properties(self):
        return {k: getattr(self, k) for k in self._property_names}

    @property
    def label(self):
        return self._label
"""
