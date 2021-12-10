from typing import List
from itertools import groupby


def encode_run_length(text: str):
    """
    Given an input string, returns the Run Length Encoded string.
    For example, if the input string is “wwwwaaadexxxxxx”,
    then the function should return “w4a3d1e1x6”

    :param text: input string to encode
    :return: run length encoded string
    """
    run_lengths = [(k, len(list(v))) for k, v in groupby(text)]
    encodings = [k + str(v) for k, v in run_lengths]
    return "".join(encodings)


def has_numbers_with_sum(numbers: List, k):
    """
    Given a list of numbers and a number k.
    returns whether any two numbers from the list add up to k.
    :param numbers: list of numbers
    :param k: expected sum of any two numbers
    :return: boolean value; True if list satisfies addition criteria
    """

    for i, x in enumerate(numbers):
        remaining = numbers[i+1:]
        for y in remaining:
            if x + y == k:
                return True
    return False


if __name__ == '__main__':
    # Tests for problem 1
    assert encode_run_length("wwwwaaadexxxxxx") == "w4a3d1e1x6"
    assert encode_run_length("wwwwaaadexxxxxxa") == "w4a3d1e1x6a1"
    assert encode_run_length("xwwwwaaadexxxxxx") == "x1w4a3d1e1x6"
    assert encode_run_length("xwwwwaaadexxxxxx ") == "x1w4a3d1e1x6 1"
    assert encode_run_length("wwwwaaadexxxxxx1") != "w4a3d1e1x6"
    assert encode_run_length("wwwwaaadexxxxxxy") != "w4a3d1e1x6"
    assert encode_run_length("Wwwwaaadexxxxxx") != "w4a3d1e1x6"
    assert encode_run_length("wwwwaAadexxxxxx") != "w4a3d1e1x6"

    # Tests for problem 2
    assert has_numbers_with_sum([10, 15, 3, 7], 17)
    assert has_numbers_with_sum([10, 15, 3, 7], 18)
    assert has_numbers_with_sum([10, 15, 3, 7], 10)
    assert not has_numbers_with_sum([10, 15, 3, 7], 19)
    assert not has_numbers_with_sum([10, 15, 3, 7], 15)
    assert not has_numbers_with_sum([10, 15, 3, 7], 20)

    # print outputs
    print(encode_run_length("wwwwaaadexxxxxx"))
    print(has_numbers_with_sum([10, 15, 3, 7], 17))
