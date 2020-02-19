import numpy as np

cube_size = 765
booster_size = 15
max_boosters = cube_size // booster_size

cube = {
    "White": 99,
    "Blue": 197,
    "Black": 296,
    "Red": 395,
    "Green": 494,
    "Fix": 586,
    "Multi": 686,
    "Colorless": 765
}


def output(boosters):
    for b in boosters:
        print(b, '\n')


def main(*args):
    qtyBoosters = -1

    while not (type(qtyBoosters) is int and (0 < qtyBoosters <= max_boosters)):
        print(f'Combien de boosters tu veux? Le maximum supporte est : {max_boosters} '
              f'\nChoisis un nb de boosters entre 1 et {max_boosters}')
        try:
            qtyBoosters = int(input())
        except EOFError:
            exit(0)

    print(f"\nVoici {qtyBoosters} boosters :\n")

    boosters = []

    for i in range(qtyBoosters):
        booster = {"White": 0, "Blue": 0, "Black": 0, "Red": 0, "Green": 0, "Fix": 0, "Multi": 0, "Colorless": 0}
        bcards = np.random.randint(0, cube_size, booster_size)
        for c in bcards:
            for (t, j) in cube.items():
                if c < j:
                    booster[t] += 1
                    break

        boosters.append(booster)

    output(boosters)


if __name__ == '__main__':
    main()
