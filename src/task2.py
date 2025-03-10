import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
        Generates a sorted list of length `quantity` from randomly selected "int"s in
        range between `min` and `max`, including both bounds.

        Returns empty list if arguments satisfy any of these conditions:
         - `min` < 1
         - `max` > 1000
         - `min` > `max`
         - `max - min + 1` < `quantity` (range does not have enough items to fill the ticket)

    :param min: low bound of the range to use for generation (not less than 1)
    :param max: high bound of the range to use for generation (not more than 1000)
    :param quantity: amount of numbers to generate
    :return: sorted list of randomly select "int"s between `min` and `max`
    """

    # checking arguments to be in the correct range
    if min < 1:
        return []
    if max > 1000:
        return []
    if min > max:
        return []
    # if we do not have enough range between `min` and `max` will not
    # be able to generate a lottery ticket without repeats
    if (max - min + 1) < quantity:
        return []

    # a set to store numbers for the result
    numbers = set()

    # we add parameters to the set until we have enough
    while len(numbers) < quantity:
        ticket = random.randint(min, max)

        numbers.add(ticket)

    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))
