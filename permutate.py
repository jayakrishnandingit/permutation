import sys
import copy
from collections import Counter, OrderedDict


def permutate(string):
    if not isinstance(string, str):
        raise Exception("Expected an str got %s." % type(string))
    if not string:
        return [string]

    char_count = OrderedDict([(char, count) for char, count in Counter(string).items()])
    char_array = [char for char in string]
    return permutate_recursively(char_array, char_count, index=0)


def permutate_recursively(result_array, char_count, index=0):
    results = []
    if index == len(result_array):
        # Okay, we looked at all characters for this order.
        results.append(''.join(result_array))
    else:
        for char, count in char_count.items():
            if count > 0:
                char_count_copy = copy.deepcopy(char_count)
                result_array_copy = copy.deepcopy(result_array)
                char_count_copy[char] -= 1
                result_array_copy[index] = char
                # recurse to place the char at next index.
                results.extend(permutate_recursively(result_array_copy, char_count_copy, index + 1))
    # no more char to look at this level, return the results.
    return results


if __name__ == '__main__':
    string = sys.argv[1]
    print(permutate(string))

