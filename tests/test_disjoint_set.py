from egbis.disjoint_set import Node, DisjointSetForest


def test_disjoint_set_forest_node_has_required_properties():
    """
    Tests that newly created set root has all required properties and default
    values.
    """
    node = Node(1)

    assert node.obj == 1
    assert node.rank == 0
    assert node.parent is node


def test_disjoint_set_forest_creation_from_list_of_values():
    """
    Tests converting list of values into group of disjoint sets.
    """
    values = [1, 2, 3]

    forest = DisjointSetForest(values)

    assert forest.num_of_sets == len(values)


def test_make_set_creates_new_tree_node():
    """
    Tests wrapping an object with Node class when a new set is created.
    """
    forest = DisjointSetForest()

    node = forest.make_set(1)

    assert node.obj == 1
    assert node.parent is node
    assert forest.num_of_sets == 1


def test_find_set_of_node():
    """
    Tests that find_set() method returns the root of the tree representing the
    set where a node belongs.
    """
    forest = DisjointSetForest()
    n1, n2, n3 = nodes = [Node(i) for i in range(3)]
    n1.parent = n2
    n2.parent = n3
    forest.sets = {n3.uid: n3}

    roots = [forest.find_set(n) for n in nodes]

    assert all([root is n3 for root in roots])


def test_union_of_two_sets_reduces_total_number_of_sets():
    """
    Tests that when two nodes are merged into one set the number of sets is
    reduced, and one of the nodes becomes the parent of the another one.
    """
    forest = DisjointSetForest()
    n1 = forest.make_set(1)
    n2 = forest.make_set(2)

    union_node = forest.union(n1, n2)

    assert forest.num_of_sets == 1
    assert union_node is n2
    assert n1.parent is n2


def test_union_of_any_two_nodes_from_distinct_sets_joins_these_sets():
    """
    Tests that iterative unification of disjoint sets merge them all into
    a single tree with a common root node.
    """
    forest = DisjointSetForest(range(8))
    nodes = list(forest.sets.values())

    while True:
        n = len(nodes)
        if n < 2:
            break
        united_nodes = []
        for i in range(0, n, 2):
            union_node = forest.union(nodes[i], nodes[i + 1])
            united_nodes.append(union_node)
        nodes = united_nodes

    assert forest.num_of_sets == 1
    assert all_nodes_have_the_same_parent(nodes)


# ----------
# Test utils
# ----------


def all_nodes_have_the_same_parent(nodes):
    return len(set([n.parent.uid for n in nodes])) == 1
