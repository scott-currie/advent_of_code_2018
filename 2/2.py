import os


def f():
    f = os.path.join(os.path.split(__file__)[0], '2.txt')
    with open(f) as infile:
        strings = [line for line in infile]

    for i in range(len(strings) - 1):
      for j in range(i + 1, len(strings)):
        if differ_by_one(strings[i], strings[j]):
            print(reduce_strings(strings[i], strings[j]))


def differ_by_one(s1, s2):
    misses = 0
    for i in range(len(s1)):
        # print(s1, s2)
        if s1[i] != s2[i]:
            # print('Bad match')
            if misses > 0:

                return False
            misses += 1
    if misses == 1:
        return True
    return False

def reduce_strings(s1, s2):
  new_str = ''
  for i in range(len(s1)):

    if s1[i] == s2[i]:
      new_str += s1[i]
  return new_str

if __name__ == '__main__':
    f()
    print(differ_by_one('abcde', 'abcdf'))