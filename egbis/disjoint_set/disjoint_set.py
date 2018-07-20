from uuid import uuid4
from collections import OrderedDict


class Node:

    def __init__(self, obj, rank=0, parent=None):
        self.obj = obj
        self.rank = rank
        self.parent = parent or self
        self.uid = str(uuid4())

    def __repr__(self):
        is_root = self is self.parent
        return f'<Node: {str(self.obj)}, root: {is_root}>'


class DisjointSetForest:

    def __init__(self, seq=None):
        seq = list(seq or [])
        sets = OrderedDict()
        for x in seq:
            node = Node(x)
            sets[node.uid] = node
        self.sets = sets

    @property
    def num_of_sets(self):
        return len(self.sets)

    def make_set(self, obj):
        new_set = Node(obj)
        self.sets[new_set.uid] = new_set
        return new_set

    def find_set(self, x: Node):
        if x is not x.parent:
            x.parent = self.find_set(x.parent)
        return x.parent

    def union(self, x: Node, y: Node):
        return self._link(self.find_set(x), self.find_set(y))

    def _link(self, x: Node, y: Node):
        if x.rank > y.rank:
            y.parent = x
            self._remove_from_roots(y.uid)
            return x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1
            self._remove_from_roots(x.uid)
            return y

    def _remove_from_roots(self, uid):
        if uid in self.sets:
            del self.sets[uid]
