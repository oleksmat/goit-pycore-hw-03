import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 0:
        return []
    if max > 1000:
        return []
    if min > max:
        return []
    if (max - min + 1) < quantity:
        return []

    numbers = set()

    while len(numbers) < quantity:
        ticket = random.randint(min, max)

        numbers.add(ticket)

    result = list(numbers)

    result.sort()

    return result

print(get_numbers_ticket(1, 49, 6))
