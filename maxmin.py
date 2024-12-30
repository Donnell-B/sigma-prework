from typing import List


def find_min_max(num_list: List[int]) -> List[int]:
    lowest = None
    highest = None

    # Iterate through array, if current num is greater or lower than what we have already then replace it
    for num in num_list:

        if lowest is None:
            lowest = num
        if highest is None:
            highest = num

        if num < lowest:
            lowest = num

        if num > highest:
            highest = num

    return [lowest, highest]


def main():
    # Test List
    list_of_nums = [
        20,
        50,
        12,
        6,
        14,
        8,
    ]

    print(find_min_max(list_of_nums))


if __name__ == '__main__':
    main()
