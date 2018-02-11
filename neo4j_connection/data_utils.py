from py2neo import Graph
import json

with open(__file__ + "/../config.json", 'r', encoding='utf-8') as f:
    config = json.load(f)

graph = Graph(**config)
