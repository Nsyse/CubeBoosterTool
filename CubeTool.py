import numpy as np
import json
import sys


class Cube:

    def __init__(self, categories: dict):
        self.categories = categories
        self.size = np.sum(list(self.categories.values()))
        self.indices = self.__build_indices()

    def __getitem__(self, item):
        return self.categories[item]

    def __build_indices(self):
        indices = {}

        total = 0
        for i, j in self.categories.items():
            indices[i] = total + j
            total += j

        return indices

    def get_rand_booster(self, size=15):

        booster = dict.fromkeys(self.categories.keys(), 0)

        for c in np.random.randint(0, self.size, size):
            for (t, j) in self.indices.items():
                if c < j:
                    booster[t] += 1
                    break
        assert np.sum(list(booster.values())) == size
        return booster

    def get_max_boosters(self, booster_size):
        return self.size // booster_size


def parse_cube_json(path: str):
    with open(path) as f:
        cube_json = json.load(f)

    if cube_json is not None:
        return Cube(cube_json)
    else:
        return None


def parse_params_json(path: str):
    with open(path) as f:
        params = json.load(f)

    if params is not None:
        return params
    else:
        return None


def query_int(msg: str):
    print(msg)
    val = input()
    try:
        return int(val)
    except ValueError:
        return None
    except EOFError:
        exit(0)


def output(boosters, print_type="BOOSTERS"):
    assert len(boosters) > 0

    print(f"\nVoici {len(boosters)} boosters :\n")

    if print_type == 'BOOSTERS':
        for b in boosters:
            print(b, '\n')
    elif print_type == 'CATEGORIES':
        for k in boosters[0].keys():
            cat = []
            for b in boosters:
                cat.append(b[k])
            print(k, ':')
            print(cat, '\n')


def build_boosters(qty_boosters: int, booster_size: int, cube: Cube):
    boosters = []

    for i in range(qty_boosters):
        boosters.append(cube.get_rand_booster(booster_size))

    return boosters


def main(*args):
    if len(args) == 0:
        cube = parse_cube_json("cube.json")
    else:
        cube = parse_cube_json(args[0])

    if len(args) < 2:
        params = parse_params_json("default.json")
    else:
        params = parse_params_json(args[1])

    qtyBoosters = None
    max_boosters = cube.get_max_boosters(params['booster_size'])

    while not (qtyBoosters is not None and (0 < qtyBoosters <= max_boosters)):
        qtyBoosters = query_int(f'Combien de boosters tu veux? Le maximum supporte est : {max_boosters}')

    output(build_boosters(qtyBoosters, params['booster_size'], cube), print_type=params['print_mode'])


if __name__ == '__main__':
    main(*sys.argv[1:])
