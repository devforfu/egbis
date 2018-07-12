from egbis.disjoint_set import DisjointSetForest


def test_disjoint_set_forest_creation_from_list_of_values():
    values = [1, 2, 3]

    forest = DisjointSetForest(values)

    assert forest.num_of_sets == len(values)
