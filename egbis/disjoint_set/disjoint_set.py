class Node:

    def __init__(self, obj, parent=None):
        self.obj = obj
        self.parent = parent or obj

    def __repr__(self):
        is_root = self.obj is self.parent
        return f'<Node: {str(self.obj)}, root: {is_root}>'


class DisjointSetForest:

    def __init__(self, seq):
        self.sets = [Node(x) for x in seq]

    @property
    def num_of_sets(self):
        return len(self.sets)

    def make_set(self, x):
        new_set = Node(x)
        self.sets.append(new_set)
