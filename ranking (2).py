import itertools as it
import os
from sys import argv


def relation(A, B):
    metric = sum([int(a >= b) for a, b in zip(A, B)])
    if metric == len(A):
        return ">"
    elif metric == 0:
        return "<"
    else:
        return "#"


def class_record():
    record = {}
    for line in open(argv[1]):
        marks = line.strip().split()
        record[marks[0]] = [int(x) for x in marks[1:]]
    return record


def relations(matrix):
    keys = list(matrix.keys())
    combo = it.combinations(keys, 2)
    rels = set([])
    for key1, key2 in combo:
        r = relation(matrix[key1], matrix[key2])
        if r == ">":
            rels.add(key1 + key2)
        elif r == "<":
            rels.add(key2 + key1)
    return list(sorted(rels))


def start_end_both(rels):
    return set([x[0] for x in rels]), set([x[1] for x in rels]), set([x[0] for x in rels]) & set([x[1] for x in rels])


def rel():
    rels = relations(class_record())
    start, ends, both = start_end_both(rels)
    removables = set([])
    rules = set([])
    for x in start:
        for y in ends:
            if x + y not in rels:
                continue
            for z in both:
                if x + z in rels and z + y in rels:
                    removables.add(x+y)
                    rules.add(x+y + " <= " + x+z + " & " + z+y)
    return rels, list(sorted(removables))), list(sorted(rules))), list(sorted(set(rels) ^ removables)))

def graph():
    rels, all_relation, removables, removal_rules, minimals=rel()
    with open("vanchi.dot", "w") as f:
        print("digraph vanchi {", file=f)
        for relation in minimal:
            print("\t%s -> %s;" % (relation[0], relation[1]), file=f)
        print("}", file=f)
    os.system("dot -T png -o vanchi.png vanchi.dot")

# import itertools as it

# def relation(A, B):
#     metric = sum([int(a >= b) for a, b in zip(A, B)])
#     if metric == len(A):
#         return ">"
#     elif metric == 0:
#         return "<"
#     else:
#         return "#"

# def rem_extras(rels):
#     start = set([x[0] for x in rels])
#     ends = set([x[1] for x in rels])
#     both = start & ends
#     removables = set([])
#     for x in start:
#         for y in ends:
#             if x + y in rels:
#                 for z in both:
#                     if x + z in rels and z + y in rels:
#                         removables.add(x + z)
#                         removables.add(y + z)
#     return rels - removables

# def all_relations(matrix):
#     rolls = matrix.keys()
#     combo = it.combinations(rolls, 2)
#     rels = set([])
#     for key1, key2 in combo:
#         r = relation(matrix[key1], matrix[key2])
#         if r == ">":
#             rels.add(key1 + key2)
#         elif r == "<":
#             rels.add(key2 + key1)
#     return rem_extras(rels)

# if _name_ == "_main_":
#     matrix = {}
#     for line in open("c:\\Users\\Kushal Beniwal\\Desktop\\ranking_students_input1.txt", "r"):
#         marks = line.strip().split()
#         matrix[marks[0]] = [int(x) for x in marks[1:]]
#     rels = all_relations(matrix)
#     print(rels)
