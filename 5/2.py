import os


def get_data(filename):
    with open(os.path.join(os.path.split(__file__)[0], filename)) as infile:
        return [c for c in infile.read().strip()]


def reduce_polymer(polymer):
    for i in range(len(polymer) - 1):
        if polymer[i] != polymer[i + 1] and (polymer[i].lower() == polymer[i + 1] or polymer[i].upper() == polymer[i + 1]):
            return polymer[:i] + polymer[i + 2:]
    return polymer


def get_units(polymer):
    return set([c.lower() for c in polymer])


def extract_unit(polymer, unit):
    return [c for c in polymer if unit != c.lower()]


if __name__ == '__main__':
    filename = '1.txt'

    base_polymer = get_data(filename)
    units = get_units(base_polymer)
    for unit in units:
        polymer = extract_unit(base_polymer, unit)
        new_poly = reduce_polymer(polymer)
        while new_poly != polymer:
            polymer = new_poly
            new_poly = reduce_polymer(polymer)
        print(unit, len(new_poly))
