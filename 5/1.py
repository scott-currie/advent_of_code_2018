import os


def get_data(filename):
    with open(os.path.join(os.path.split(__file__)[0], filename)) as infile:
        return [c for c in infile.read().strip()]

def reduce_polymer(polymer):
    for i in range(len(polymer) - 1):
        if polymer[i] != polymer[i + 1] and (polymer[i].lower() == polymer[i + 1] or polymer[i].upper() == polymer[i + 1]):
            return polymer[:i] + polymer[i + 2:]
    return polymer

if __name__ == '__main__':
    filename = '1.txt'
    polymer = get_data(filename)
    new_polymer = reduce_polymer(polymer)
    # print(polymer)
    while polymer != new_polymer:
        polymer = new_polymer
        new_polymer = reduce_polymer(polymer)
    print(len(new_polymer))
